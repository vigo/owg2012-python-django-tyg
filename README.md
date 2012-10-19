owg2012-pyhton-django-tyg
=========================

Özgür Web Günleri 2012, Python ve Django ile Testle Yürüyen Geliştirme Sunum ve örnekler

## Örnek Kodlar

Unit test için:

    slide_12__docstring_test.py
    slide_15__unit_test.py
    slide_17__unit_test_decorators.py
    slide_25__first_doctest.py

tesleri çalıştırmak için:

    python slide_15__unit_test.py
    python -m unittest slide_15__unit_test
    python -m unittest slide_15__unit_test.TestCalculator
    python -m unittest slide_15__unit_test.TestCalculator.test_addition

gibi kullanabilirsiniz.

## Django Uygulaması

`sample_code/sample_blog_app/blog` altında; `tests` dizini... Unit Test için : `tests.py`,
**selenium** testi için `tests_selenium.py` dosyalarını kullanabilirsiniz.