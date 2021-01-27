
const path = require('path');

module.exports = {
  entry: {
    main: './shortener/frontend/src/main.js',
  },
  output: {
    path: path.join(__dirname, './shortener/frontend/static/frontend/js/'),
    filename: 'shortener.bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(png|woff|woff2|eot|ttf|svg)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 100000,
            },
          },
        ],
      },
    ],
  },
};
