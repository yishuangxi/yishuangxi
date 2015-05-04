
(function($){
    var editor;
    KindEditor.ready(function (K) {
        editor = K.create('#kindeditor', {
            allowFileManager: true
        });
    });

    $(function(){
        var $publish = $("#publish");
        var $cate = $("select[name=cate]");
        var $title = $("input[name=title]");
        $publish.click(function(){
            var title = $title.val();
            var cate = $cate.val();
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
        
        var $newCate = $(".new-cate");
        var $newCateContainer = $(".new-cate-container");
        var $cateCancel = $(".cate-cancel");
        var $cateSave = $(".cate-save");
        var $cateName = $("input[name=cate_name]");
        $newCate.click(function(){
            $newCateContainer.show();
        });
        $cateCancel.click(function(){
            $newCateContainer.hide();
        });
        $cateSave.click(function(){
            $.ajax("/cate",{
                type:"POST",
                data:{
                    name:$cateName.val()
                },
                success:function(data){
                    if(data.success){
                        $cate.prepend("<option value='"+data.data.id+"'>"+data.data.name+"</option>")[0].selectedIndex=0;
                        $newCateContainer.hide();
                    }else{
                        alert(data.msg || "保存失败，请重试！");
                    }
                },
                error:function(){
                    
                }
            });
        });
        
        var $draft = $("#draft");
        $draft.click(function(){
            var title = $title.val();
            var cate = $cate.val();
            var content = editor.html();
            var draft = 1;
            $.ajax("/publish",{
                type:"POST",
                data:{
                    title:title,
                    cate:cate,
                    content:content,
                    draft:draft
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

