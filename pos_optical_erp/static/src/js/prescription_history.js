odoo.define('pos_optical_erp.prescription_history',function(require){
"use strict";

var gui = require('point_of_sale.gui');
var chrome = require('point_of_sale.chrome');
var core = require('web.core');
var models = require('point_of_sale.models');
var pos_screens = require('point_of_sale.screens');
var QWeb = core.qweb;
var _t = core._t;

models.load_models({
        model:  'dr.prescription',
        fields: ['name','dr','customer','checkup_date','test_type','prescription_type','state'],
        loaded: function(self,products){
            self.products = products;
        },
    });

var PrescriptionButton = pos_screens.ActionButtonWidget.extend({
    template: 'PrescriptionButton',
    button_click: function(){
            this.gui.show_screen('product-list');
            var self = this;
    }
});

pos_screens.define_action_button({
    'name': 'PrescriptionButton',
    'widget':PrescriptionButton,
});


var ProductWidget = pos_screens.ScreenWidget.extend({
    template: 'Product-ListWidget-Custom',
    init: function(parent, options){
        this._super(parent, options);
    },

    show: function(){
            var self = this;
            this._super();
            this.renderElement();
            this.$('.back').click(function(){
                self.gui.show_screen('products');
            });

            var products = []
            for (var i=0;i < this.pos.products.length ;i++){
                      products.push(this.pos.products[i]);
            }

            self.products = products;
            this.render_list(products);
            this.$('.products-list-contents').delegate('.productlines','click',function(event){
                self.line_select(event,$(this.parentElement.parentElement),parseInt($(this.parentElement.parentElement).data('id')))
            });


            var search_timeout = null;

            if(this.pos.config.iface_vkeyboard && this.chrome.widget.keyboard){
                this.chrome.widget.keyboard.connect(this.$('.searchbox input'));
            }

            this.$('.searchbox input').on('keyup',function(event){
                clearTimeout(search_timeout);
                var query = this.value;
                search_timeout = setTimeout(function(){
                    self.perform_search(query,event.which === 13);
                },70);
            });

            this.$('.searchbox .search-clear').click(function(){
                self.clear_search();
            });
    },

    perform_search: function(query){
            var products;
            if(query){
               products = this.search_products(query);
                this.render_list(products);
            }else{
                products = this.pos.products;
                this.render_list(products);
    }
    },

    render_list: function(products){
            var length = products.length
            var contents = this.$el[0].querySelector('.products-list-contents');
            contents.innerHTML = "";
            for(var i = 0, len = Math.min(products.length); i < len; i++){
                var product    = products[i];
                var product_line_html = QWeb.render('ProductsLine',{widget: this, product:products[i]});
                var product_line = document.createElement('tbody');
                product_line.innerHTML = product_line_html;
                product_line = product_line.childNodes[1];
                contents.appendChild(product_line);
            }
    },

    search_products: function(query){
            try {
                var re = RegExp(query);
            }catch(e){
                return [];
            }
            var results = [];
            for (var product_id in this.pos.products){
                var r = re.exec(this.pos.products[product_id]['name']);
                var g = re.exec(this.pos.products[product_id]['dr']);
                if(r || g){
                results.push(this.pos.products[product_id]);
                }
            }
            return results;

        },









});

gui.define_screen({name:'product-list',widget:ProductWidget});

});


