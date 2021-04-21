odoo.define('pos_prescription_creation',function(require) {

    var gui = require('point_of_sale.gui');
    var chrome = require('point_of_sale.chrome');
    var PopupWidget = require('point_of_sale.popups');
    var screens = require('point_of_sale.screens');
    var popups = require('point_of_sale.popups');
    var core = require('web.core');
    var models = require('point_of_sale.models');
    var rpc = require('web.rpc');
    var utils = require('web.utils');
    var QWeb = core.qweb;
    var _t = core._t;

    var ProductWidget = screens.ScreenWidget.extend({
        template: 'Product-ListWidget-Custom',
        init: function(parent, options){
            this._super(parent, options);
        },
        show: function(){
            var self = this;
            var optical_orders = [];
            this._super();
            this.renderElement();
            this.$('.back').click(function(){
                self.gui.show_screen('products');
            });
            var order = this.pos.get_order();
            optical_order_ids = order.get_screen_data('params')
            if (optical_order_ids)
                for (var i=0; i < optical_order_ids.length; i++)
                    optical_orders.push(self.pos.optical.order_by_id[optical_order_ids[i].id])
            else
                var optical_orders = self.pos.optical.all_orders
            this.render_list(optical_orders, undefined, undefined);
            var search_timeout = null;
//            if(this.pos.config.iface_vkeyboard && this.chrome.widget.keyboard){
//                this.chrome.widget.keyboard.connect(this.$('.searchbox input'));
//            }
            this.$('.products-list-contents').on('click', '.productlines', function(event){
                self.line_select(event,$(this),parseInt($(this).data('id')));
            });
            this.$('.searchbox_date').keyup(function() {
                self.render_list(optical_orders, this.childNodes[1].value, undefined);
            });
            this.$('.searchbox_client').keyup(function() {
                self.render_list(optical_orders, undefined, this.childNodes[1].value);
            });
            this.$('.searchbox .search-clear').click(function(){
                self.clear_search();
            });
        },
        line_select: function(event,$line,id){
            var self = this;
    		optical_order =  self.pos.optical.order_by_id[id]
        	var contents = this.$('.optical_order-details-content');
    	    if (parseInt($('.prescription_receipt_details').data('id')) !== id){
        	    contents.empty();
        		contents.append($(QWeb.render('PrescriptionShowTable',{widget:this, optical_order:optical_order})));
        	}
    	    else
        	    contents.empty();
        },
        render_list: function(optical_orders, date_value, client_value){
            var self = this
            var length = optical_orders.length
            var contents = this.$el[0].querySelector('.products-list-contents');
            contents.innerHTML = "";
            if (client_value)
                optical_orders = optical_orders.filter(function(el){return el.customer[1].toLowerCase().includes(client_value.toLowerCase())})
            if (date_value)
                optical_orders = optical_orders.filter(function(el){return el.checkup_date.toLowerCase().includes(date_value.toLowerCase())})
            len = Math.min(optical_orders.length)-1;
            for(var i = len ; i >= 0; i--){
                var optical_order = optical_orders[i];
                var optical_orders_line_html = QWeb.render('ProductsLine',{widget: this, product:optical_order});
                var optical_orders_line = document.createElement('tbody');
                optical_orders_line.innerHTML = optical_orders_line_html;
                optical_orders_line = optical_orders_line.childNodes[1];
                contents.appendChild(optical_orders_line);
            }
            this.$('.pos_optical_copy').click(function(event) {
                var order = self.pos.get_order();
                optical_order = self.pos.optical.order_by_id[parseInt($(this).data('orderId'))];
                $('.optical_prescription').text(optical_order.name);
                order.set_optical_reference(optical_order);
                self.gui.back();
            });
            this.$('.pos_optical_print').click(function(event) {
                self.gui.show_screen('PrescriptionReceipt',parseInt($(this).data('orderId')));
            });
        },
    });
    gui.define_screen({name:'product-list',widget:ProductWidget});

    screens.ClientListScreenWidget.include({
        events: {
            'click .prescription_count_btn': 'prescription_count_btn',
    	},
        display_client_details: function(visibility,partner,clickpos){
            var self = this;
            var searchbox = this.$('.searchbox input');
            var contents = this.$('.client-details-contents');
            var parent   = this.$('.client-list').parent();
            var scroll   = parent.scrollTop();
            var height   = contents.height();

            contents.off('click','.button.edit');
            contents.off('click','.button.save');
            contents.off('click','.button.undo');
            contents.on('click','.button.edit',function(){ self.edit_client_details(partner); });
            contents.on('click','.button.save',function(){ self.save_client_details(partner); });
            contents.on('click','.button.undo',function(){ self.undo_client_details(partner); });
            this.editing_client = false;
            this.uploaded_picture = null;
            count = 0
            if (partner)
                count = self.pos.optical.all_orders.filter(function(el){return el.customer[0] === partner.id}).length
            if(visibility === 'show'){
                contents.empty();
                contents.append($(QWeb.render('ClientDetails',{widget:this,partner:partner,prescription_count:count})));
                var new_height   = contents.height();
                if(!this.details_visible){
                    // resize client list to take into account client details
                    parent.height('-=' + new_height);
                    if(clickpos < scroll + new_height + 20 ){
                        parent.scrollTop( clickpos - 20 );
                    }else{
                        parent.scrollTop(parent.scrollTop() + new_height);
                    }
                }else{
                    parent.scrollTop(parent.scrollTop() - height + new_height);
                }
                this.details_visible = true;
                this.toggle_save_button();
            } else if (visibility === 'edit') {
                // Connect the keyboard to the edited field
                if (this.pos.config.iface_vkeyboard && this.chrome.widget.keyboard) {
                    contents.off('click', '.detail');
                    searchbox.off('click');
                    contents.on('click', '.detail', function(ev){
                        self.chrome.widget.keyboard.connect(ev.target);
                        self.chrome.widget.keyboard.show();
                    });
                    searchbox.on('click', function() {
                        self.chrome.widget.keyboard.connect($(this));
                    });
                }
                this.editing_client = true;
                contents.empty();
                contents.append($(QWeb.render('ClientDetailsEdit',{widget:this,partner:partner,prescription_count:count})));
                this.toggle_save_button();
                // Browsers attempt to scroll invisible input elements
                // into view (eg. when hidden behind keyboard). They don't
                // seem to take into account that some elements are not
                // scrollable.
                contents.find('input').blur(function() {
                    setTimeout(function() {
                        self.$('.window').scrollTop(0);
                    }, 0);
                });
                contents.find('.client-address-country').on('change', function (ev) {
                    var $stateSelection = contents.find('.client-address-states');
                    var value = this.value;
                    $stateSelection.empty()
                    $stateSelection.append($("<option/>", {
                        value: '',
                        text: 'None',
                    }));
                    self.pos.states.forEach(function (state) {
                        if (state.country_id[0] == value) {
                            $stateSelection.append($("<option/>", {
                                value: state.id,
                                text: state.name
                            }));
                        }
                    });
                });
                contents.find('.image-uploader').on('change',function(event){
                    self.load_image_file(event.target.files[0],function(res){
                        if (res) {
                            contents.find('.client-picture img, .client-picture .fa').remove();
                            contents.find('.client-picture').append("<img src='"+res+"'>");
                            contents.find('.detail.picture').remove();
                            self.uploaded_picture = res;
                        }
                    });
                });
            } else if (visibility === 'hide') {
                contents.empty();
                parent.height('100%');
                if( height > scroll ){
                    contents.css({height:height+'px'});
                    contents.animate({height:0},400,function(){
                        contents.css({height:''});
                    });
                }else{
                    parent.scrollTop( parent.scrollTop() - height);
                }
                this.details_visible = false;
                this.toggle_save_button();
            }
        },
        prescription_count_btn: function(){
//        $(this)[0].$el[0].children[0].children[1].childNodes[1].childNodes[1].children[0].children[0].children[0].children[2].children[0].dataset['id']
            optical_orders = this.pos.optical.all_orders.filter(function(el){return el.customer[0] === $('.prescription_count_btn').data('id')})
            this.gui.show_screen('product-list', optical_orders);
        },
    });
});