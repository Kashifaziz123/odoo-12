odoo.define('product_multi_uom_pos.multi_uom',function(require) {
"use strict";

var gui = require('point_of_sale.gui');
var PopupWidget = require('point_of_sale.popups');
var core = require('web.core');
var chrome = require('point_of_sale.chrome')
var models = require('point_of_sale.models');
var rpc = require('web.rpc');
var QWeb = core.qweb;
var _t = core._t;
var pos_screens = require('point_of_sale.screens');

models.load_models({
        model:  'optical.dr',
        fields: ['name'],
        loaded: function(self,categories){
            self.categories = categories;
        },
    });

models.load_models({
        model:  'product.product',
        fields: ['name'],
        loaded: function(self,customers){
            self.customers = customers;
        },
    });

chrome.OrderSelectorWidget.include({
    renderElement: function(){
        var self = this;
        this._super();
        var categ = [];
        var partners = [];
        for (var i in self.pos.categories){
            categ.push(self.pos.categories[i].name);
        }
        for (var i in self.pos.customers){
            partners.push(self.pos.customers[i].name);
        }
        this.$('.add-product').click(function(event){
            self.gui.show_popup('multi_uom_screen',{
                'category': categ,
                'partner':partners
            });
        });
    },
});



var MultiUomWidget = PopupWidget.extend({
    template: 'MultiUomWidget',

    events: {
        'click .button.cancel':  'click_cancel',
        'click .button.confirm': 'click_confirm',
    },

    click_cancel: function(){
        this.gui.close_popup();
        if (this.options.cancel) {
            this.options.cancel.call(this);
        }
    },

});
gui.define_popup({name:'multi_uom_screen', widget: MultiUomWidget});




//pos_screens.ActionpadWidget.include({
//    /*opening the wizard on button click*/
//    renderElement: function() {
//        this._super();
//        var self = this;
//        var doc = [];
//        for (var i in self.pos.doctors){
//            doc.push(self.pos.doctors[i].name);
//        }
//        this.$('.multi-uom-span').click(function(){
//            console.log('mehdi',doc)
//            self.gui.show_popup('multi_uom_screen',{
//                'optometrist':doc
//
//            });
//
//        });
//    }
//});

});