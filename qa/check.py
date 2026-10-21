import pathlib,re,sys,subprocess
root=pathlib.Path(__file__).resolve().parents[1]
html=list(root.rglob('*.html'))
missing=[]
for f in html:
 t=f.read_text(encoding='utf-8')
 for link in re.findall(r'(?:src|href)=["\']([^"\']+)["\']',t):
  if link.startswith(('http:','https:','#','data:','mailto:')):continue
  target=(f.parent/link.split('?')[0]).resolve()
  if not target.exists():missing.append((str(f.relative_to(root)),link))
assert not missing,missing
for f in root.rglob('*.js'):
 r=subprocess.run(['node','--check',str(f)],capture_output=True,text=True)
 assert r.returncode==0,(str(f),r.stderr)
print('PASS:',len(html),'HTML files, local links, JS syntax')
