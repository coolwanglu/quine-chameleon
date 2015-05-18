#!/usr/bin/env python3

import os
import sys
import random
import shutil
import re

SRC_DIR = 'src'
DST_DIR = 'build'

LANGS=[] # all languages implemented
BUILD_LANGS=[] # languages to build

DATA={}
DATASTRING=''

LANGINDEXES={} # the index of language to output in ouroboros

LANGNAMES={
  'c':'C',
  'coffee':'CoffeeScript',
  'cpp':'C++',
  'cs':'C#',
  'el':'Emacs Lisp',
  'lua':'Lua',
  'java':'Java',
  'js':'JavaScript',
  'pl':'Perl',
  'py':'Python',
  'rb':'Ruby',
  'scala':'Scala',
}

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
  DST_PREFIX = 'qc.'

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
        .replace('LANGINDEXxFIELDCOUNT', str(LANGINDEXES[lang]*FIELDCOUNT))\
        .replace('LANGCOUNT_1', str(len(LANGS)-1))\
        .replace('LANGCOUNT', str(len(LANGS)))\
        .replace('FIELDCOUNT', str(FIELDCOUNT))

def build_string():
  s = [];
  for lang_name in LANGS:
    source_code = DATA[lang_name]
    if CMD.startswith('multiquines'):
      s.append(lang_name)
    s.append(source_code.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n').replace('DATA','\\0'))
  s.append('')
  global DATASTRING
  DATASTRING = '\\0'.join(s)

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
