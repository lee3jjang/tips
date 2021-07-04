Argparse 사용법
================

사용 예시
~~~~~~~~~~

.. code-block:: python

    parser = argparse.ArgumentParser(
        prog='MyProgram',
        description='Process Some Integers.',
    )

    parser.add_argument('-s', '--src', nargs='?', help='src help', required=False, default=argparse.SUPPRESS)
    args = parser.parse_args()

    if hasattr(args, 'src'):
        print(args.src)

.. list-table:: **add_argument 설명**
    :widths: auto
    :header-rows: 1

    * - 매개변수
      - 의미
    * - nargs=?
      - ?으로 하면 키만 넣고 값 안 넣을 수 있음
    * - required=False
      - 무조건 넣어야 하는 argument인지 결정
    * - default=argparse.SUPPRESS
      - argument 입력 안 할 때 None 도 안 보이게 함