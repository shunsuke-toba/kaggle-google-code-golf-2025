import os, shutil
os.mkdir('submission')
for i in range(1, 401):
    shutil.copy(f'{i:03d}/3_submission.py', f'submission/task{i:03d}.py')
shutil.make_archive('submission', 'zip', 'submission')
shutil.rmtree('submission')