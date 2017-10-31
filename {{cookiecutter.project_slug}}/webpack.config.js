var webpack = require('webpack')
var S3Plugin = require('webpack-s3-plugin')
var CompressionPlugin = require('compression-webpack-plugin')

module.exports = {
    entry: './{{cookiecutter.project_slug}}/static/main.js',
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        'scss': 'vue-style-loader!css-loader!sass-loader',
                        'sass': 'vue-style-loader!css-loader!sass-loader?indentedSyntax'
                    }
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]?[hash]'
                }
            }
        ]
    },
    resolve: {
        alias: {'vue$': 'vue/dist/vue.esm.js'}
    },
    devServer: {
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
    performance: {hints: false},
    watchOptions: {poll: 1000},
    devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production') {
    module.exports.devtool = '#source-map'
    module.exports.output = {
        path: '/',
        publicPath: 'http://localhost:3000/static/dist/',
        filename: 'build.js'
    },
    module.exports.module.rules = (module.exports.module.rules || []).concat([
        {
            enforce: 'pre',
            test: /\.vue$/,
            loader: 'string-replace-loader',
            query: {
                search: new RegExp('/static/', 'g'),
                replace: 'https://' + process.env.AWS_STORAGE_BUCKET_NAME + '.s3.' + process.env.AWS_STORAGE_BUCKET_REGION + '.amazonaws.com/static/'
            }
        }
    ]),
    module.exports.plugins = [
        new webpack.DefinePlugin({'process.env': {NODE_ENV: '"production"'}}),
        new webpack.LoaderOptionsPlugin({minimize: true}),
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: true,
            compress: {warnings: false}
        }),
        new CompressionPlugin({asset: '[path].gz'}),
        new S3Plugin({
            include: /.*\js/,
            s3Options: {
                accessKeyId: process.env.AWS_ACCESS_KEY_ID,
                secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
                region: process.env.AWS_STORAGE_BUCKET_REGION
            },
            s3UploadOptions: {
                Bucket: process.env.AWS_STORAGE_BUCKET_NAME,
                Expires: new Date(Date.now() + (30 * 24 * 60 * 60 * 1000)),
                CacheControl: 'max-age=604800, no-transform, public',
                ContentEncoding: 'gzip'
            },
            basePath: 'static/dist/'
        })
    ]
} else {
    module.exports.plugins = [
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.LoaderOptionsPlugin({vue: {loader: {js: 'babel-loader'}}})
    ],
    module.exports.output = {
        path: '/app/{{cookiecutter.project_slug}}/static/dist/',
        publicPath: 'http://localhost:3000/static/dist/',
        filename: 'build.js'
    }
}
