import shutil
shutil.rmtree('docs')
shutil.copytree('./_build/html', './docs')