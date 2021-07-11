파이썬 패키지 배포하는법
=========================

1. ``setup.py`` 을 만들고 아래처럼 입력

.. code-block:: python

    from setuptools import setup, find_packages

    setup(
        name='tips',
        version='0.1.0',
        author='lee3jjang',
        author_email='lee3jjang@gmail.com',
        description='Tips library',
        long_description='This is tips library for programming',
        url='https://github.com/lee3jjang/tips',
        packages=find_packages(),
        python_requires=">=3.6",
        zip_safe=False,
    )

2. ``python setup.py bdist_wheel`` 입력하면 dist 폴더에 .whl 파일 생성

.. note::

    패키지명은 setup.py 에서 정하는거(모듈은 폴더명 따라감)
    
