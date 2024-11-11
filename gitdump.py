import os
import argparse
import sys
import re
import sys
import datetime
import requests
from rich.progress import Progress

def logo():
  logo = '''
█▀▀ █ ▀█▀ █▀▄ █░█ █▀▄▀█ █▀█  version
█▄█ █ ░█░ █▄▀ █▄█ █░▀░█ █▀▀  2.0.0
A Divinemonk creation!
  '''
  return logo

def datetime_init():
  datetime_str = str(datetime.datetime.now()).replace(' ', '_')
  re_result = re.findall(r'(\d{6})', datetime_str)
  datetime_str = datetime_str.strip(re_result[0]).strip('.')
  return datetime_str

def github_data(username):
  # https://stackoverflow.com/questions/27331849/github-api-v3-doesnt-show-all-user-repositories
  repo_list = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100") # &page=2
  rl = list(repo_list.json())
  
  if len(rl)<3 and rl[0] == 'message':
    print('[gitdump] (error)> Github Username Not Found')
    sys.exit(1)
  
  return rl

def mkdir(dir):
  try:
    os.mkdir(dir)
  except:
    print('[gitdump] (error)> Folder Not Created')
    exit()

def clone(dir, url):
  try:
    os.system(f'cd {dir} && git clone {url} --quiet')
  except:
    print('[gitdump] (error)> Unable to Clone given URL')
    exit()

def dump(dir, data):
  mkdir(dir)
  with Progress() as progress:
    dump_progress_bar = progress.add_task("[red]\\[gitdump] (status)> \n", total=len(data))

    for i in range(len(data)):
      progress.update(dump_progress_bar, advance=1)
      url = data[i]['html_url']
      print(f'[gitdump] (dumping)> {url}')
      clone(dir, url)

def parser(help=False):
  parser = argparse.ArgumentParser(description='Dump all repos of a github account at once.')
  parser.add_argument('-u', '--username', dest='username',
                      help='uername of the github account')
  parser.add_argument('-l', '--location', dest='location',
                      help='location to save dumped repos')
  
  def help_msg():
    parser.print_help(sys.stderr)
    exit()

  if help:
    help_msg()
  elif len(sys.argv)==1:
    help_msg()

  return parser.parse_args()

def main():
  print(logo())
  args = parser()
  if args.username and args.location:
    username = args.username
    location = args.location
    
    data = github_data(username)
    datetime_str = datetime_init()
    dir = f'{location}{username}_{datetime_str.replace(':', '-')}'
   
    dump(dir, data)
    
  else:
    print("[gitdump]> github-username or output-file-location parameters missing!\n")
    parser(True)

if __name__ == "__main__":
  main()
