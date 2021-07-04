import shutil
shutil.rmtree('docs', ignore_errors=True)
shutil.move('_build/html', 'docs')
shutil.rmtree('_build')