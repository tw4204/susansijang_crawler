docker run --rm -it\
  -w /source \
  -v $PWD/source:/source \
  susansijang_crawler:1.0 python3 crawler.py
