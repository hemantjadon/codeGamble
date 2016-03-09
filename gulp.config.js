module.exports = function (){
    var config = {
        allLessFiles : 'codeGamble/dev/**/*.less',
        lessOutputPath : 'codeGamble/dist',
        allJsFiles : 'codeGamble/dev/**/*.js',
        jsOutputPath: 'codeGamble/dist',
        allJSXFiles: 'codeGamble/dev/**/*.jsx',
        jsxOutputPath : 'codeGamble/dist'
    }
    
    return config;
}