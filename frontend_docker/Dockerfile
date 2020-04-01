# hub.docker.comから公式で用意されたイメージをベースとする
FROM node:10.13-alpine
# カレントディレクトリを app に
WORKDIR /frontend
# vue-cliのダウンロード
RUN npm install -g @vue/cli@3.9.3 \
  && npm install --save axios vue-axios
# デフォルトで node が起動するので sh を代わりに起動
CMD ["sh"]