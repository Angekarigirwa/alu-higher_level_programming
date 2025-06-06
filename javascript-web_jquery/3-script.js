#!/usr/bin/node
const $ = window.$;
$('div#red_header').click(function () {
  $('header').addClass('red');
});
