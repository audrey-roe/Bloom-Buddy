<script type="text/javascript">
    jQuery(document).ready(function($) {
        $(window).load(function() {
            $('.btnNext').click(function(){
                $('.nav-tabs > .active').next('li').find('a').trigger('click');
            });
            $('.btnPrevious').click(function(){
                $('.nav-tabs > .active').prev('li').find('a').trigger('click');
            });

            $('[data-toggle="tooltip"]').tooltip();

        })
    })
    </script>