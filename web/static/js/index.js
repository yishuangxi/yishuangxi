(function($){
    $(function(){
        var hash = location.hash;
        var iframe = $("iframe[name=iframe]")[0];
        var href = "/pages/latest";
        if(hash){
            href = hash.replace("#", "");
            
        }
        iframe.src = href;
        
        var $a = $("a[target=iframe]");
        $a.click(function(e){
            var iframe = top.$("iframe[name=iframe]")[0];
            var $this = $(this);
            var href = $this.attr("href");
            top.location.hash='#'+href;
            iframe.src = href;
            
            e.preventDefault();
            return false;
        });
    });
})(jQuery);