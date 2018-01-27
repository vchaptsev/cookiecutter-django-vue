var webpack = require('webpack')
var BundleTracker  = require('webpack-bundle-tracker')
{% if cookiecutter.static_and_media == 'Amazon S3 (static and media)' -%}
var S3Plugin = require('webpack-s3-plugin')
var CompressionPlugin = require('compression-webpack-plugin')
var amazonPath = 'https://' + process.env.AWS_STORAGE_BUCKET_NAME + '.s3.' + process.env.AWS_STORAGE_BUCKET_REGION + '.amazonaws.com/static/dist/'
{% endif %}

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
    plugins: [
        new BundleTracker({filename: './webpack.json'})
    ],
    resolve: {
        alias: {'vue$': 'vue/dist/vue.esm.js'}
    }
}

// ==================== PRODUCTION SETTINGS ====================
if (process.env.NODE_ENV === 'production') {
    module.exports.devtool = '#source-map'
    module.exports.output = {
        {% if cookiecutter.static_and_media == 'Amazon S3 (static and media)' -%}
        path: '/',
        publicPath: amazonPath,
        {% else %}
        path: '/app/staticfiles/dist/',
        publicPath: 'http://localhost:3000/static/dist/',
        {% endif %}
        filename: '[name]-[hash].js'
    },
    {% if cookiecutter.static_and_media == 'Amazon S3 (static and media)' -%}
    module.exports.module.rules.push(
        {
            enforce: 'pre',
            test: /\.vue$/,
            loader: 'string-replace-loader',
            query: {
                search: new RegExp('/static/', 'g'),
                replace: amazonPath
            }
        }
    ),
    {% endif %}
    module.exports.plugins.push(
        new webpack.DefinePlugin({'process.env': {NODE_ENV: '"production"'}}),
        new webpack.LoaderOptionsPlugin({minimize: true}),
        new webpack.optimize.UglifyJsPlugin({sourceMap: true, compress: {warnings: false}}),
        {% if cookiecutter.static_and_media == 'Amazon S3 (static and media)' -%}
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
        {% endif %}
    )
}

// ==================== DEVELOPMENT SETTINGS ====================
if (process.env.NODE_ENV === 'development') {
    module.exports.devtool = '#eval-source-map',
    module.exports.output = {
        path: '/app/{{cookiecutter.project_slug}}/static/dist/',
        publicPath: 'http://localhost:3000/static/dist/',
        filename: '[name]-[hash].js'
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
