#!/usr/bin/env python3

import subprocess
import sys
import os
import shutil
import time

TMP_DIR = '/tmp/quine-chameleon'
try: os.mkdir(TMP_DIR)
except: pass

#entry: compile-command, run-command
#see also compile_file() and run_file()
languages = {
  'awk': ['', 'gawk -f {0}'],
  'c': ['gcc -O3 -pedantic -Wall -Werror -std=c99 -o {1} {0}', '{0}'],
  'coffee': ['', 'coffee {0}'],
  'cpp': ['g++ -O3 -pedantic -Wall -Werror -std=c++11 -o {1} {0}', '{0}'],
  'cs': ['mcs -out:{1} {0}', 'mono {0}'],
  'el': ['', 'emacs --batch --quick --script {0}'],
  'go': ['', 'go run {0}'],
  'lua': ['', 'lua {0}'],
  'java': ['javac {2}/qc.java', 'cd {1} && java qc'],
  'js': ['', 'nodejs {0}'],
  'pl': ['', 'perl6 {0}'],
  'py': ['', 'python3 {0}'], 
  'rb': ['', 'ruby {0}'],
  'rkt': ['', 'racket -q {0}'],
  'scala': ['scalac {0}', 'scala qc'],
  'vala': ['valac -o {1} {0}', '{0}'],
}

signatures = {} 

def get_src_filename(lang):
  return os.path.join('build', 'qc.' + lang)

def compile_file(lang, src_fn, bin_fn, logfile=None):
  compile_cmd = languages[lang][0]
  if compile_cmd:
    if lang == 'java': #hack for java
      tmp_java_fn = os.path.join(TMP_DIR, 'qc.java')
      if src_fn != tmp_java_fn:
        shutil.copyfile(src_fn, tmp_java_fn)
        src_fn = tmp_java_fn

    subprocess.check_call(compile_cmd.format(src_fn, bin_fn, TMP_DIR), shell=True, stdout=logfile, stderr=logfile)
    return True
  else:
    return False

def run_file(lang, src_fn, bin_fn, target_lang='', logfile=None):
  compile_cmd, run_cmd = languages[lang]
  return subprocess.check_output(run_cmd.format((bin_fn if compile_cmd else src_fn), TMP_DIR) + ' ' + target_lang, shell=True, stderr=logfile)

def test(languages_used):
  for lang in languages_used:
    if lang not in languages:
      print('Unknown language: '+lang)
      sys.exit(-1)

  all_test_good = True
  with open('log.txt', 'w') as logf:
    for lang in languages_used:
      compile_cmd, run_cmd = languages[lang]
      print('Testing ' + lang + ' ...', end='', flush=True)
      src_fn = get_src_filename(lang)
      bin_fn = os.path.join(TMP_DIR, 'qc-bin')

      all_good = True
      try:
        compiled = compile_file(lang, src_fn, bin_fn, logf)
      except:
        print('cannot compile!')
        all_good = False
        continue

      if CMD == 'multiquines':
        for target_lang in languages.keys():
          try:
            output = run_file(lang, src_fn, bin_fn, target_lang, logf)
          except:
            print('execution failed with:' + target_lang)
            all_good = False
            break
          with open(get_src_filename(target_lang), 'rb') as srcf:
            if output != srcf.read():
              print('output not identical:' + target_lang)
              logf.write('output of ' + lang + ':\n')
              logf.write(output.decode('latin-1') + '\n\n')
              all_good = False
              break

      else:
        sorted_langs = sorted(languages.keys())
        repeat = 3 if CMD == 'chameleon' else 1
        for i in range(repeat):
          try:
            output = run_file(lang, src_fn, bin_fn, '', logf)
          except:
            print('execution failed')
            all_good = False
            break
          try:
            target_lang = detect_language(output, False)
            if CMD == 'ouroboros':
              i1 = sorted_langs.index(lang)
              i2 = sorted_langs.index(target_lang)
              if i2 != (i1+1)%len(sorted_langs):
                print('output not in alphabetical order: ' + target_lang)
                logf.write('output of ' + lang + ':\n')
                logf.write(output.decode('latin-1') + '\n\n')
                all_good=False
                break
          except:
            print('output with unknown language')
            logf.write('output of ' + lang + ':\n')
            logf.write(output.decode('latin-1') + '\n\n')
            all_good = False
            break

      if all_good: print('ok!')
      else: all_test_good = False

  if not all_test_good:
    print('See log.txt for more detail')
    sys.exit(-1)

def detect_language(s, quick_check):
  sig_len = 13
  if len(signatures) == 0:
    for lang in languages:
      with open(get_src_filename(lang), 'rb') as f:
        f.seek(-sig_len, 2)
        sig = f.read(sig_len) 
        if sig in signatures:
          print('signature is not long enough:',sig_len,lang,signatures[sig])
        signatures[sig]=lang

  try:
    lang = signatures[s[-sig_len:]]
    if quick_check:
      return lang
    with open(get_src_filename(lang), 'rb') as f:
      if f.read() != s:
        raise Exception('File content not identical')
    return lang
  except KeyError:
    raise Exception('Cannot detect type')

def run_through(filename, max_iteration):
  stats = {}
  cur_iteration = 0
  with open(filename, 'rb') as f:
    cur_source = f.read()
  bin_fn = os.path.join(TMP_DIR, 'qc-bin')
  with open(os.path.join(TMP_DIR, 'log.txt'), 'w') as logf:
    try:
      while max_iteration == 0 or cur_iteration < max_iteration:
        start_time = time.time()
        filename = os.path.join(TMP_DIR, 'qc')
        try:
          lang = detect_language(cur_source, True)
        except:
          with open(filename, 'wb') as f:
            f.write(cur_source)
          raise
          sys.exit(-1)
        stats[lang] = stats.get(lang,0) + 1
        print(str(cur_iteration) + ': ' + lang)
        filename += '.' + lang
        with open(filename, 'wb') as f:
          f.write(cur_source)
        compile_file(lang, filename, bin_fn, logf)
        cur_source = run_file(lang, filename, bin_fn, '', logf)
        cur_iteration += 1
        # some languages' rand seed is based on seconds, need to refresh it
        while time.time() < start_time + 1:
          time.sleep(0.1)

    except KeyboardInterrupt:
      # we could be interrupted at anywhere, so re-calculate the sum
      total_run = sum(stats.values())
      runs = sorted(stats.items(), key=lambda x:x[1])
      h1 = 'Language'
      h2 = 'Count'
      w1 = max(len(i[0]) for i in runs)
      w1 = max(w1, len(h1))
      w2 = max(len(str(i[1])) for i in runs)
      w2 = max(w2, len(h2))
      print()
      print('Statistics:')
      print('{:{w1}} {:{w2}}     %'.format(h1, h2, w1=w1, w2=w2))
      for l,c in runs:
        print('{:>{w1}} {:^{w2}} {:4.1f}%'.format(l, c, c/total_run*100, w1=w1, w2=w2))
      print()

"""
Usage:

  ./test.py chameleon|ouroboros|random-ouroboros|multiquines [lang1 [lang2 ...]]

    Test the specified mode with specified languages
    Need to prepare the source files first, for language detection (see Makefile)

  ./test.py dance [file [max_iteration]]

    Run the file, execute the output, and repeat
    Need to prepare the source files first, for language detection (see Makefile)

"""

if len(sys.argv) < 2:
  print('need an argument')

CMD = sys.argv[1]
if CMD in ['chameleon', 'ouroboros', 'random-ouroboros', 'multiquines']:
  languages_used = sorted(languages.keys()) if len(sys.argv) == 2 else sys.argv[2:]
  test(languages_used)
elif CMD == 'dance':
  filename = sys.argv[2] if len(sys.argv) > 2 else 'chameleon.py'
  if not os.path.isfile(filename):
    print('Cannot find file: ' + filename)
    sys.exit(-1)
  max_iteration = 0
  if len(sys.argv) > 3:
    try:
      max_iteration = int(sys.argv[3])
    except ValueError:
      print('Bad number:' + sys.argv[3])
      sys.exit(-1)
  run_through(filename, max_iteration)
else:
  print('Unknown argument: ' + CMD)
  sys.exit(-1)
