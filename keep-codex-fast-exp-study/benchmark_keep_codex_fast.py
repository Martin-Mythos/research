#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, os, sqlite3, tempfile, time, sys
from pathlib import Path

SCRIPT = Path('external_repo/scripts/keep_codex_fast.py').resolve()

def load_module():
    spec = importlib.util.spec_from_file_location('keep_codex_fast', SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.modules['keep_codex_fast']=m
    spec.loader.exec_module(m)
    m.codex_processes_running = lambda: []
    m.top_node_processes = lambda details=False: m.report('top_node_processes skipped_in_bench')
    return m

def make_home(root: Path, n=2000):
    ch = root/'.codex'; (ch/'sessions/2026/01/01').mkdir(parents=True)
    (ch/'.codex-global-state.json').write_text('{"pinned-thread-ids":[]}', encoding='utf-8')
    (ch/'config.toml').write_text('', encoding='utf-8')
    db = ch/'state_5.sqlite'
    conn = sqlite3.connect(db)
    conn.execute('create table threads (id text primary key, title text, rollout_path text, cwd text, updated_at integer, archived_at integer, archived integer)')
    old = int(time.time()-40*86400)
    for i in range(n):
        tid = f'{i:012d}-aaaa-aaaa-aaaa-aaaaaaaaaaaa'[:36]
        p = ch/f'sessions/2026/01/01/rollout-{i}.jsonl'
        p.write_text('{"type":"x"}\n', encoding='utf-8')
        os.utime(p, (old, old))
        conn.execute('insert into threads values (?,?,?,?,?,?,?)', (tid, f't{i}', str(p), r'C:\tmp', old, None, 0))
    conn.commit(); conn.close()
    return ch

def timed_run(m, args):
    t0=time.perf_counter(); rc=m.run(args); dt=time.perf_counter()-t0; return rc, dt

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--threads', type=int, default=2000); a=ap.parse_args()
    m=load_module()
    with tempfile.TemporaryDirectory() as td:
        ch=make_home(Path(td), a.threads)
        backup=Path(td)/'backup'
        common=dict(details=False,wait_for_codex_exit=False,codex_home=str(ch),backup_root=str(backup),archive_older_than_days=10,worktree_older_than_days=7,rotate_logs_above_mb=0)
        modes=[('report',False,False),('backup_only',False,True),('apply',True,False)]
        for name,apply,bo in modes:
            args=argparse.Namespace(apply=apply,backup_only=bo,**common)
            rc,dt=timed_run(m,args)
            print(f'{name}\trc={rc}\tsec={dt:.3f}')
if __name__=='__main__': main()
