requirejs.config({
    baseUrl:"/static/js",
    paths:{
        jquery:"core/jquery",
        kindeditor:"plugins/kindeditor/kindeditor"
    },
    shim: {
        'kindeditor': {
            exports: 'kindeditor'
        }
    }
});  
define(["jquery","kindeditor"],function($, KindEditor){
    console.log($);
    console.log(KindEditor);
    KindEditor.ready(function (K) {
        var editor = K.create('#kindeditor', {
            allowFileManager: true
        });
    });
});