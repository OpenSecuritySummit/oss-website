if($.cookie('themeCSSpath')){$('link#theme-stylesheet').attr('href',$.cookie('themeCSSpath'))}
if($.cookie('themeLayout')){$('body').addClass($.cookie('themeLayout'))}
$(function(){sliderHomepage()
sliders()})
function contactForm(){var form=$('.contact-form')
form.submit(function(){$this=$(this)
$.post($(this).attr('action'),$this.serialize(),function(){$this[0].reset()
$('#contact-message').html('<div class="alert alert-success" role="alert"><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>Thank you for getting in touch. We will get back to you soon!</div>').fadeIn()},'json')
return false})}
function demo(){if($.cookie('themeCSSpath')){$('link#theme-stylesheet').attr('href',$.cookie('themeCSSpath'))}
$('#colour').change(function(){if($(this).val()!==''){var themeCSSpath='css/style.'+$(this).val()+'.css'
$('link#theme-stylesheet').attr('href',themeCSSpath)
$.cookie('themeCSSpath',themeCSSpath,{expires:365,path:'/'})}
return false})
$('#layout').change(function(){if($(this).val()!==''){var themeLayout=$(this).val()
$('body').removeClass('wide')
$('body').removeClass('boxed')
$('body').addClass(themeLayout)
$.cookie('themeLayout',themeLayout,{expires:365,path:'/'})}
return false})}
function sliderHomepage(){if($('#slider').length){$('#slider').owlCarousel({autoPlay:3000,items:4,itemsDesktopSmall:[900,3],itemsTablet:[600,3],itemsMobile:[500,2]})}}
function sliders(){if($('.owl-carousel').length){$('.customers').owlCarousel({items:3,itemsDesktopSmall:[990,3],itemsTablet:[768,2],itemsMobile:[480,1]})
$('.testimonials').owlCarousel({items:4,itemsDesktopSmall:[990,3],itemsTablet:[768,2],itemsMobile:[480,1]})
$('.project').owlCarousel({navigation:true,navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],slideSpeed:300,paginationSpeed:400,autoPlay:true,stopOnHover:true,singleItem:true,afterInit:'',lazyLoad:true})
$('.homepage').owlCarousel({navigation:false,navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],slideSpeed:2000,paginationSpeed:1000,autoPlay:true,stopOnHover:true,singleItem:true,lazyLoad:false,addClassActive:true,afterInit:function(){},afterMove:function(){}})}}
function menuSliding(){$('.dropdown').on('show.bs.dropdown',function(){if($(window).width()>750){$(this).find('.dropdown-menu').first().stop(true,true).slideDown()}else{$(this).find('.dropdown-menu').first().stop(true,true).show()}})
$('.dropdown').on('hide.bs.dropdown',function(){if($(window).width()>750){$(this).find('.dropdown-menu').first().stop(true,true).slideUp()}else{$(this).find('.dropdown-menu').first().stop(true,true).hide()}})}
function animations(){var delayTime=0
$('[data-animate]').css({opacity:'0'})
$('[data-animate]').waypoint(function(){delayTime+=150
$(this).delay(delayTime).queue(function(next){$(this).toggleClass('animated')
$(this).toggleClass($(this).data('animate'))
delayTime=0
next()})},{offset:'90%',triggerOnce:true})
$('[data-animate-hover]').hover(function(){$(this).css({opacity:1})
$(this).addClass('animated')
$(this).removeClass($(this).data('animate'))
$(this).addClass($(this).data('animate-hover'))},function(){$(this).removeClass('animated')
$(this).removeClass($(this).data('animate-hover'))})}
function animationsSlider(){var delayTimeSlider=400
$('.owl-item:not(.active) [data-animate-always]').each(function(){$(this).removeClass('animated')
$(this).removeClass($(this).data('animate-always'))
$(this).stop(true,true,true).css({opacity:0})})
$('.owl-item.active [data-animate-always]').each(function(){delayTimeSlider+=500
$(this).delay(delayTimeSlider).queue(function(){$(this).addClass('animated')
$(this).addClass($(this).data('animate-always'))
console.log($(this).data('animate-always'))})})}
function counters(){$('.counter').counterUp({delay:10,time:1000})}
function pictureZoom(){$('.product .image, .post .image, .photostream div').each(function(){var imgHeight=$(this).find('img').height()
$(this).height(imgHeight)})}
function fullScreenContainer(){var screenWidth=$(window).width()+'px'
var screenHeight='500px'
if($(window).height()>500){screenHeight=$(window).height()+'px'}
$('#intro, #intro .item').css({width:screenWidth,height:screenHeight})}
function utils(){$('[data-toggle="tooltip"]').tooltip()
$('#checkout').on('click','.box.shipping-method, .box.payment-method',function(){var radio=$(this).find(':radio')
radio.prop('checked',true)})
$('.box.clickable').on('click',function(){window.location=$(this).find('a').attr('href')})
$('.external').on('click',function(e){e.preventDefault()
window.open($(this).attr('href'))})
$('.scroll-to, .scroll-to-top').click(function(event){var fullUrl=this.href
var parts=fullUrl.split('#')
if(parts.length>1){scrollTo(fullUrl)
event.preventDefault()}})
function scrollTo(fullUrl){var parts=fullUrl.split('#')
var trgt=parts[1]
var targetOffset=$('#'+trgt).offset()
var targetTop=targetOffset.top-100
if(targetTop<0){targetTop=0}
$('html, body').animate({scrollTop:targetTop},1000)}}
function productDetailGallery(confDetailSwitch){$('.thumb:first').addClass('active')
var timer=setInterval(autoSwitch,confDetailSwitch)
$('.thumb').click(function(e){switchImage($(this))
clearInterval(timer)
timer=setInterval(autoSwitch,confDetailSwitch)
e.preventDefault()})
$('#mainImage').hover(function(){clearInterval(timer)},function(){timer=setInterval(autoSwitch,confDetailSwitch)})
function autoSwitch(){var nextThumb=$('.thumb.active').closest('div').next('div').find('.thumb')
if(nextThumb.length===0){nextThumb=$('.thumb:first')}
switchImage(nextThumb)}
function switchImage(thumb){$('.thumb').removeClass('active')
var bigUrl=thumb.attr('href')
thumb.addClass('active')
$('#mainImage img').attr('src',bigUrl)}}
function productDetailSizes(){$('.sizes a').click(function(e){e.preventDefault()
$('.sizes a').removeClass('active')
$('.size-input').prop('checked',false)
$(this).addClass('active')
$(this).next('input').prop('checked',true)})}
$.fn.alignElementsSameHeight=function(){$('.same-height-row').each(function(){var maxHeight=0
var children=$(this).find('.same-height')
children.height('auto')
if($(window).width()>768){children.each(function(){if($(this).innerHeight()>maxHeight){maxHeight=$(this).innerHeight()}})
children.innerHeight(maxHeight)}
maxHeight=0
children=$(this).find('.same-height-always')
children.height('auto')
children.each(function(){if($(this).height()>maxHeight){maxHeight=$(this).innerHeight()}})
children.innerHeight(maxHeight)})}
var windowWidth
$(function(){windowWidth=$(window).width()
$(this).alignElementsSameHeight()
pictureZoom()})
$(window).resize(function(){var newWindowWidth=$(window).width()
if(windowWidth!==newWindowWidth){setTimeout(function(){$(this).alignElementsSameHeight()
fullScreenContainer()
pictureZoom()},205)
windowWidth=newWindowWidth}});$(document).ready(function(){if($(window).width()>960){var leftHeight=$('.aside_bx').height();$('.aside_bx').attr('data-height',leftHeight);var url=document.location.toString();if(url.match('#')){$('.nav-tabs a[href="#'+url.split('#')[1]+'"]').tab('show');}
$('.nav-tabs a').on('shown.bs.tab',function(e){window.location.hash=e.target.hash;})
$('a[data-toggle=tab]').click(function(){var elemId=$(this).attr('href');var rightHeight=$(elemId).height();if((rightHeight>leftHeight)){$('.aside_bx').height(rightHeight+20);}else{$('.aside_bx').height($('.aside_bx').attr('data-height'));}});}
$('#myCarousel').carousel({interval:3000})
$('#myCarousel,#myCarousel2').on('slid.bs.carousel',function(){});});