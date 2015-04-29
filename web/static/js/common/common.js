(function($){
    $(function(){
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