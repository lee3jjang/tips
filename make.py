import os
import shutil
os.makedirs('_static', exist_ok=True)
shutil.rmtree('docs', ignore_errors=True)
shutil.move('_build/html', 'docs')
shutil.rmtree('_build')