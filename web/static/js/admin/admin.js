
(function($){
    var editor;
    KindEditor.ready(function (K) {
        editor = K.create('#kindeditor', {
            allowFileManager: true
        });
    });

    $(function(){
        var $publish = $("#publish");
        $publish.click(function(){
            var title = $("input[name=title]").val();
            var cate = $("select[name=cate]").val();
            var content = editor.html();
            
            $.ajax("/publish",{
                type:"POST",
                data:{
                    title:title,
                    cate:cate,
                    content:content
                },
                success:function(){
                    alert("发表成功");
                },
                error:function(){
                    alert("error !");
                }
            });            
        });
    });
})(jQuery);

