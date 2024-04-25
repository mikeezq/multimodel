jQuery(document).ready(function($) {
   
   'use strict';

//SMOOTH SCROLL
smoothScroll.init({
     speed: 3000,
     easing: 'easeInOutCubic',
     updateURL: false,
     callbackBefore: function(toggle, anchor) {},
     callbackAfter: function(toggle, anchor) {}
});

//ANIMATIONS
var wow = new WOW(
    {
        boxClass:     'wow',      // animated element css class (default is wow)
        offset:       0,          // distance to the element when triggering the animation (default is 0)
        animateClass: 'animated', // animation css class (default is animated)
        mobile:       false        // trigger animations on mobile devices (true is default)
      }
    );
wow.init();


//HEADER ANIMATION
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
        } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
        }
});

//FULLSCREEN SLIDER
$('#slides').superslides({
    animation: 'fade',
    pagination:false
    
});

//VIDEO

   // Basic FitVids Test
        $(".container").fitVids();
        // Custom selector and No-Double-Wrapping Prevention Test
        $(".container").fitVids({ customSelector: "iframe[src^='http://socialcam.com']"});
        // Popup Video


//PORTFOLIO
(function($, window, document, undefined) {
    'use strict';

    var gridContainer = $('#grid-container'),
        filtersContainer = $('#filters-container'),
        wrap, filtersCallback;


    /*********************************
        init cubeportfolio
     *********************************/
    gridContainer.cubeportfolio({
        layoutMode: 'grid',
        rewindNav: true,
        scrollByPage: false,
        defaultFilter: '*',
        animationType: 'quicksand',
        gapHorizontal: 35,
        gapVertical: 25,
        gridAdjustment: 'responsive',
        mediaQueries: [{
            width: 1100,
            cols: 4
        }, {
            width: 800,
            cols: 3
        }, {
            width: 500,
            cols: 2
        }, {
            width: 320,
            cols: 1
        }],
        caption: 'zoom',
        displayType: 'lazyLoading',
        displayTypeSpeed: 100,

        // lightbox
        lightboxDelegate: '.cbp-lightbox',
        lightboxGallery: true,
        lightboxTitleSrc: 'data-title',
        lightboxCounter: '<div class="cbp-popup-lightbox-counter">{{current}} of {{total}}</div>',

        // singlePage popup
        singlePageDelegate: '.cbp-singlePage',
        singlePageDeeplinking: true,
        singlePageStickyNavigation: true,
        singlePageCounter: '<div class="cbp-popup-singlePage-counter">{{current}} of {{total}}</div>',
        singlePageCallback: function(url, element) {
            // to update singlePage content use the following method: this.updateSinglePage(yourContent)
            var t = this;

            $.ajax({
                    url: url,
                    type: 'GET',
                    dataType: 'html',
                    timeout: 5000
                })
                .done(function(result) {
                    t.updateSinglePage(result);
                })
                .fail(function() {
                    t.updateSinglePage("Error! Please refresh the page!");
                });
        },

        // single page inline
        singlePageInlineDelegate: '.cbp-singlePageInline',
        singlePageInlinePosition: 'above',
        singlePageInlineInFocus: true,
        singlePageInlineCallback: function(url, element) {
            // to update singlePage Inline content use the following method: this.updateSinglePageInline(yourContent)
        }
    });


    /*********************************
        add listener for filters
     *********************************/
    if (filtersContainer.hasClass('cbp-l-filters-dropdown')) {
        wrap = filtersContainer.find('.cbp-l-filters-dropdownWrap');

        wrap.on({
            'mouseover.cbp': function() {
                wrap.addClass('cbp-l-filters-dropdownWrap-open');
            },
            'mouseleave.cbp': function() {
                wrap.removeClass('cbp-l-filters-dropdownWrap-open');
            }
        });

        filtersCallback = function(me) {
            wrap.find('.cbp-filter-item').removeClass('cbp-filter-item-active');
            wrap.find('.cbp-l-filters-dropdownHeader').text(me.text());
            me.addClass('cbp-filter-item-active');
            wrap.trigger('mouseleave.cbp');
        };
    } else {
        filtersCallback = function(me) {
            me.addClass('cbp-filter-item-active').siblings().removeClass('cbp-filter-item-active');
        };
    }

    filtersContainer.on('click.cbp', '.cbp-filter-item', function() {
        var me = $(this);

        if (me.hasClass('cbp-filter-item-active')) {
            return;
        }

        // get cubeportfolio data and check if is still animating (reposition) the items.
        if (!$.data(gridContainer[0], 'cubeportfolio').isAnimating) {
            filtersCallback.call(null, me);
        }

        // filter the items
        gridContainer.cubeportfolio('filter', me.data('filter'), function() {});
    });


    /*********************************
        activate counter for filters
     *********************************/
    gridContainer.cubeportfolio('showCounter', filtersContainer.find('.cbp-filter-item'), function() {
        // read from url and change filter active
        var match = /#cbpf=(.*?)([#|?&]|$)/gi.exec(location.href),
            item;
        if (match !== null) {
            item = filtersContainer.find('.cbp-filter-item').filter('[data-filter="' + match[1] + '"]');
            if (item.length) {
                filtersCallback.call(null, item);
            }
        }
    });


    /*********************************
        add listener for load more
     *********************************/
    $('.cbp-l-loadMore-link').on('click.cbp', function(e) {
        var t = $(this),
            clicks;

        e.preventDefault();

        if (t.hasClass('cbp-l-loadMore-stop')) {
            return;
        }

        // get the number of times the loadMore link had been clicked
        clicks = $.data(this, 'numberOfClicks');
        clicks = (clicks) ? ++clicks : 1;
        $.data(this, 'numberOfClicks', clicks);

        // set loading status
        t.addClass('cbp-l-loadMore-loading');

        // perform ajax request
        $.ajax({
            url: t.attr('href'),
            type: 'GET',
            dataType: 'HTML'
        }).done(function(result) {
            var items, itemsNext;

            // find current container
            items = $(result).filter(function() {
                return $(this).is('div' + '.cbp-loadMore-block' + clicks);
            });

            gridContainer.cubeportfolio('appendItems', items.html(),
                function() {
                    // put the original message back
                    t.removeClass('cbp-l-loadMore-loading');

                    // check if we have more works
                    itemsNext = $(result).filter(function() {
                        return $(this).is('div' + '.cbp-loadMore-block' + (clicks + 1));
                    });

                    if (itemsNext.length === 0) {
                        t.addClass('cbp-l-loadMore-stop');
                    }

                });

        }).fail(function() {
            // error
        });

    });

})(jQuery, window, document);

/*RELATED WORKS*/
(function($, window, document, undefined) {
    'use strict';
    // init cubeportfolio
    $('#related-container').cubeportfolio({
        layoutMode: 'slider',
        drag: true,
        auto: false,
        autoTimeout: 5000,
        autoPauseOnHover: true,
        showNavigation: true,
        showPagination: false,
        rewindNav: false,
        scrollByPage: false,
        gridAdjustment: 'responsive',
        mediaQueries: [{
            width: 1100,
            cols: 4
        }, {
            width: 800,
            cols: 3
        }, {
            width: 500,
            cols: 2
        }, {
            width: 320,
            cols: 1
        }],
        gapHorizontal: 0,
        gapVertical: 25,
        caption: 'overlayBottomReveal',
        displayType: 'lazyLoading',
        displayTypeSpeed: 100,

        // lightbox
        lightboxDelegate: '.cbp-lightbox',
        lightboxGallery: true,
        lightboxTitleSrc: 'data-title',
        lightboxCounter: '<div class="cbp-popup-lightbox-counter">{{current}} of {{total}}</div>',

        // singlePage popup
        singlePageDelegate: '.cbp-singlePage',
        singlePageDeeplinking: true,
        singlePageStickyNavigation: true,
        singlePageCounter: '<div class="cbp-popup-singlePage-counter">{{current}} of {{total}}</div>',
        singlePageAnimation: 'fade',
        singlePageCallback: function(url, element) {
            // to update singlePage content use the following method: this.updateSinglePage(yourContent)
            var indexElement = $(element).parents('.cbp-item').index(),
                item = singlePage.eq(indexElement);

            this.updateSinglePage(item.html());
        }
    });

})(jQuery, window, document);

//End
});

//CONTACT FORM FUNCTION
    var contact_send = function(){    
    'use strict';    
    var name    = $("#name").val();
    var email   = $("#email").val();
    var subject   = $("#subject").val();
    var message = $("#message").val();
    
    if ( name=="" ){ alert("Введите имя!"); $("#name").focus(); }
    else if ( email=="" ){ alert("Не правильный E-mail!"); $("#email").focus(); }
    else if ( subject=="" ){ alert("Введите тему!"); $("#subject").focus(); }
    else if ( message=="" ){ alert("Введите сообщение"); $("#message").focus(); }
    else {
        $.post("contact.send.php", { name:name, email:email, subject:subject, message:message }, function( result ){
            if ( result=="SUCCESS" ){
                alert("Your contact form is sent.");
                setTimeout(function(){
                    $("#name").val("");
                    $("#email").val("");
                    $("#subject").val("");
                    $("#message").val("");
                }, 3000);
            } else {
                alert("Your contact form isn't sent. Please check fields and try again.");
            }
        });
    }
};

//PRELOADING
$(window).load(function(){

    //PRELOADER
    $('#preload').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
    
});

//POPUP VIDEO

$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false


});

//GOOGLE MAP
function init_map() {
    var myOptions = {
        zoom: 14,
        center: new google.maps.LatLng(55.749792, 37.632495), //change the coordinates
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        scrollwheel: false,
        mapTypeControl: false,
        styles: [{featureType:'all',stylers:[{saturation:-100},{gamma:0.50}]}]
    };
     
    var map = new google.maps.Map(document.getElementById("gmap_canvas"), myOptions);
    var marker = new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(55.749792, 37.632495) //change the coordinates
    });
    var infowindow = new google.maps.InfoWindow({
        content: "<b>html6.com.ru</b><br/>Россия<br/> Москва"  //add your address
    });
    google.maps.event.addListener(marker, "click", function () {
        infowindow.open(map, marker);
    });
    infowindow.open(map, marker);
    }
    if ($("#gmap_canvas").length > 0){
    google.maps.event.addDomListener(window, 'load', init_map);
    }