var webpack = require('webpack')

// ==================== MAIN SETTINGS ====================
module.exports = {
    entry: ['babel-polyfill', './{{cookiecutter.project_slug}}/static/main.js'],
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        'scss': 'vue-style-loader!css-loader!sass-loader',
                        'sass': 'vue-style-loader!css-loader!sass-loader?indentedSyntax'
                    },
                    transformToRequire: {video: 'src', source: 'src', img: 'src', image: 'xlink:href'}
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
                loader: 'url-loader',
                options: {limit: 10000, name: '[name].[hash:7].[ext]'}
            },
            {
                test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/,
                loader: 'url-loader',
                options: {limit: 10000, name: '[name].[hash:7].[ext]'}
            },
            {
                test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
                loader: 'url-loader',
                options: {limit: 10000, name: '[name].[hash:7].[ext]'}
            }
        ]
    },
    plugins: [],
    resolve: {
        alias: {'vue$': 'vue/dist/vue.esm.js'}
    }
}

// ==================== PRODUCTION SETTINGS ====================
if (process.env.NODE_ENV === 'production') {
    module.exports.devtool = '#source-map'
    module.exports.output = {
        path: '/app/staticfiles/dist/',
        publicPath: 'http://localhost:3000/staticfiles/dist/',
        filename: 'bundle.js'
    },
    module.exports.plugins.push(
        new webpack.DefinePlugin({'process.env': {NODE_ENV: '"production"'}}),
        new webpack.LoaderOptionsPlugin({minimize: true}),
        new webpack.optimize.UglifyJsPlugin({sourceMap: true, compress: {warnings: false}})
    )
}

// ==================== DEVELOPMENT SETTINGS ====================
if (process.env.NODE_ENV === 'development') {
    module.exports.devtool = '#eval-source-map',
    module.exports.output = {
        path: '/app/{{cookiecutter.project_slug}}/staticfiles/dist/',
        publicPath: 'http://localhost:3000/staticfiles/dist/',
        filename: 'bundle.js'
    },
    module.exports.plugins.push(
        new webpack.DefinePlugin({'process.env': {NODE_ENV: '"development"'}}),
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.LoaderOptionsPlugin({vue: {loader: {js: 'babel-loader'}}})
    ),
    module.exports.devServer = {
        historyApiFallback: true,
        noInfo: true,
        host: '0.0.0.0',
        port: 3000,
        hot: true,
        filename: 'bundle.js',
        headers: {
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With'
        }
    },
    module.exports.performance = {hints: false},
    module.exports.watchOptions = {poll: 1000}
}
