#!/usr/bin/env python3

import os
import sys
import random
import shutil
import re
import string

SRC_DIR = 'src'
DST_DIR = 'build'

LANGS=[] # all languages implemented
BUILD_LANGS=[] # languages to build

DATA={}
DATASTRING=''
UNUSED_CHARS=[]
DELIMETER='\\t'
DELIMETERCODE=ord('\t')

LANGINDEXES={} # the index of language to output in ouroboros

LANGNAMES={
  'awk':'AWK',
  'c':'C',
  'coffee':'CoffeeScript',
  'clj':'Clojure',
  'cpp':'C++',
  'cs':'C#',
  'd':'D',
  'el':'Emacs Lisp',
  'fs':'F#',
  'go':'Go',
  'hs':'Haskell',
  'hx':'Haxe',
  'lua':'Lua',
  'm':'Objective C',
  'ml':'OCaml',
  'java':'Java',
  'js':'JavaScript',
  'octave':'Octave',
  'pl':'Perl',
  'py':'Python',
  'R':'R',
  'rb':'Ruby',
  'rkt':'Racket',
  'scala':'Scala',
  'vala':'Vala',
}

def escape_string(s):
  return s.replace('\\','\\\\').replace('\n','\\n').replace('"','\\"')

def configure():
  global CMD
  CMD = sys.argv[1] if len(sys.argv) > 1 else 'chameleon'
  if CMD not in [
    'chameleon', 'chameleon-all', 
    'ouroboros', 'ouroboros-all', 
    'random-ouroboros', 'random-ouroboros-all',
    'multiquines', 'multiquines-all'
  ]:
    print('Unknown mode: ' + CMD)
    sys.exit(-1)

  global SRC_PREFIX
  if CMD.startswith('multiquines'):
    SRC_PREFIX = 'multiquines.'
  else:
    SRC_PREFIX = 'chameleon.'

  global DST_PREFIX
  DST_PREFIX = 'QC.'

  global FIELDCOUNT
  FIELDCOUNT = 2 if CMD != 'multiquines' else 3
  global BUILD_LANGS
  if not CMD.endswith('-all'):
    BUILD_LANGS = ['py']

def collect_languages():
  for filename in os.listdir(SRC_DIR):
    if not filename.startswith(SRC_PREFIX): continue
    LANGS.append(filename[len(SRC_PREFIX):])
  LANGS.sort()

def preprocess():
  if CMD.startswith('ouroboros'):
    for i in range(len(LANGS)):
      LANGINDEXES[LANGS[i]] = (i+1)%len(LANGS)
  elif CMD.startswith('random-ouroboros'):
    l = list(range(len(LANGS)))
    random.shuffle(l)
    for i in range(len(LANGS)):
      LANGINDEXES[LANGS[i]] = l[i]
  else:
    for i in range(len(LANGS)):
      LANGINDEXES[LANGS[i]] = i

  def replace(match):
    match = match.groups()
    if match[0] not in CMD: return ''
    return match[1]

  pattern = re.compile(r'{{{(chameleon|ouroboros):([^}]*)}}}')
  
  for lang in LANGS:
    with open(os.path.join(SRC_DIR, SRC_PREFIX+lang)) as f:
      DATA[lang] = pattern.sub(replace, f.read())\
        .replace('ENTRYINDEX+1', str(LANGINDEXES[lang]*FIELDCOUNT+1))\
        .replace('ENTRYINDEX', str(LANGINDEXES[lang]*FIELDCOUNT))\
        .replace('LANGCOUNT-1', str(len(LANGS)-1))\
        .replace('LANGCOUNT', str(len(LANGS)))\
        .replace('FIELDCOUNT+1', str(FIELDCOUNT+1))\
        .replace('FIELDCOUNT', str(FIELDCOUNT))\
        .replace('DELIMETERCODE', str(DELIMETERCODE))\
        .replace('DELIMETER', DELIMETER)
      assert('\t' not in DATA[lang])


#  used = set()
#  for c in "\"\'\0\t\n\r\x0b\x0c":
#    used.add(c)
#  for lang in LANGS:
#    for c in escape_string(DATA[lang])\
#      .replace('DATA','')\
#      .replace('DELIMETERCODE','')\
#      .replace('DELIMETER','')\
#      .replace('LENGTH+1',''):
#      used.add(c)
#  for c in string.printable:
#    if c not in used:
#      UNUSED_CHARS.append(c)
#
#  global DELIMETER
#  DELIMETER = UNUSED_CHARS.pop()

def build_string():
  s = [];
  for lang_name in LANGS:
    source_code = DATA[lang_name]
    if CMD.startswith('multiquines'):
      s.append(lang_name)
    s.append(escape_string(source_code).replace('DATA', DELIMETER))
  global DATASTRING
  DATASTRING = DELIMETER.join(s)

  c = DATASTRING.count('LENGTH+1')
  l = len(DATASTRING) - len('LENGTH+1')*c
  l += (len(str(l))+1)*c + 1
  DATASTRING = DATASTRING.replace('LENGTH+1', str(l))
  for lang in LANGS:
    DATA[lang] = DATA[lang].replace('LENGTH+1', str(l))


def analyze():
  return

  #table[i][j]: max length of matching suffixes ends at i and j
  table = [[0 for _1 in range(len(DATASTRING))] for _2 in range(len(data))]
  for i in range(len(DATASTRING) - 1):
    for j in range(i+1, len(DATASTRING)):
      if DATASTRING[i] == data[j]:
        table[i][j] = 1 if i==0 else table[i-1][j-1] + 1

  max_len = 0

  # adjacent-list version of table
  l_suffix = [{} for _ in range(len(DATASTRING))]
  for i in range(len(DATASTRING)):
    d = l_suffix[i]
    for j in range(i+1, len(DATASTRING)):
      ll = table[i][j]
      if ll > 1:
        if ll in d:
          d[ll].append(j)
        else:
          d[ll] = [j]

        if ll > max_len:
          max_len = ll

  # entry: [start, len, count]
  # there may be duplicates
  entries = []
  for i in range(len(DATASTRING)):
    for le, li in l_suffix[i].items():
      entries.append([i-le+1, le, len(li)])
  
  entries.sort(key=lambda x:-(x[1]-1)*(x[2]-1))
  used = []
  saved_bytes = 0;
  for s,l,c in entries:
    ss = DATASTRING[s:s+l]
    for us in used:
      if us in ss or ss in us:
        break;
    else:
      used.append(ss)
      saved_bytes += l*c-l-c-2
      print(ss,c,l*c-l-c-2,'->',s,l)
      if len(used) >= unused_count:
        break
  print('Total saved:',saved_bytes)
        

def write_files():
  try: os.mkdir(DST_DIR)
  except: pass

  global BUILD_LANGS
  if len(BUILD_LANGS) == 0:
    BUILD_LANGS = LANGS

  for lang in BUILD_LANGS:
    with open(os.path.join(DST_DIR, DST_PREFIX+lang), 'w') as f:
      f.write(DATA[lang].replace('DATA', DATASTRING))

def build_readme():
  with open('README.md', 'rb') as f:
    lines = f.readlines()
  try:
    marker1 = b'<!--LANGUAGES-BEGIN-->\n'
    marker2 = b'<!--LANGUAGES-END-->\n'
    lines1 = lines[ : 1+lines.index(marker1)]
    lines2 = lines[lines.index(marker2) : ]
    sizes = []
    for lang in LANGS:
      sizes.append([lang, len(DATA[lang]) - len('DATA') + len(DATASTRING)])
    sizes.sort(key=lambda x:x[1])
    size_lines = [b'\\# | Language | Size | Suffix\n', b'--- | --- | --- | ---\n']
    for i,l in enumerate(sizes):
      size_lines.append('{0} | {1} | {2} | {3}\n'.format(i+1, LANGNAMES[l[0]], l[1], l[0]).encode())
      
    with open('README.md', 'wb') as f:
      f.write(b''.join(lines1 + size_lines + lines2))
  except:
    print('Failed to build README!')
    raise

configure()
collect_languages()
preprocess()
build_string()
write_files()

if not CMD.endswith('-all'):
  shutil.copyfile(os.path.join(DST_DIR, DST_PREFIX+'py'), CMD+'.py') 
  shutil.rmtree(DST_DIR)

if CMD.startswith('chameleon'):
  build_readme()
