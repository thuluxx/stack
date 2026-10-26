
from pathlib import Path
import ast


def analyze_repository(repo_path:str):
    files=list(Path(repo_path).rglob('*.py'))
    results=[]
    funcs=classes=0
    for f in files:
        src=f.read_text(encoding='utf-8',errors='ignore')
        tree=ast.parse(src)
        fn=sum(isinstance(n,ast.FunctionDef) for n in ast.walk(tree))
        cl=sum(isinstance(n,ast.ClassDef) for n in ast.walk(tree))
        funcs+=fn
        classes+=cl
        results.append({'file':str(f),'functions':fn,'classes':cl})
    return {'files':len(files),'functions':funcs,'classes':classes,'analysis':results}
