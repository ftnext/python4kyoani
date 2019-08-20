=================
python4kyoani
=================

Pythonで、京都アニメーションにお返しするプロジェクト

機能 (Features)
=================

任意の画像から PrayForKyoani と文字を入れた画像を新たに作成します

.. image:: https://raw.githubusercontent.com/ftnext/2019_slides/f63ec19ffa798391be80fbb7b412268eacf964de/stapy_Aug_PrayForKyoani/assets/pray_candles.jpg

インストール方法 (Installation)
==================================

.. code-block:: shell

    $ pip install python4kyoani

使い方 (Usage)
=================

.. code-block:: shell

    $ py4ka ./candle.jpg
    $ open pray_candle.jpg

このプロジェクトって何よ？ (About this project)
===================================================

| 2019/07/18 京都アニメーションに放火事件という悲劇が起きました。
| プロジェクト発案者nikkieは、京都アニメーションの大ファンのPython使いです。
| 京都アニメーションの作品に、ときに奮い立たされ、ときに癒やされ、エンジニアとして前に進んできました。
| Python使いとしての今があるのは、京都アニメーションからいただいたもののおかげでもあると思っています。

| この事件で辛いのは、自分が心から大切にしている存在が傷つけられたことです。
| 時間が経つにつれて、優秀なアニメーターの方々を失ったことが分かり、悲しみが重なっていきます。
| それでも、前を向く時間を増やすという選択をしたくて、私ができることで京都アニメーションへの祈りをなんとかして表現したいと思いました。
| 私ができること＝Pythonで京都アニメーションからいただいたものへのお返しを試みていきます（今後も機能を追加します）。
| このプロジェクトで、悲しみに沈む京アニファンを一人でも、ほんの少しの時間でも、前を向くお手伝いができたら、それ以上に嬉しいことはありません。

Python for Kyoani.

開発に参加したい方へ (Development)
==================================

.. code-block:: shell

    $ git clone git@github.com:ftnext/python4kyoani.git python4kyoani
    $ cd python4kyoani
    $ pip install -e .[dev]
