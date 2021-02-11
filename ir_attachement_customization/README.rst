Guideline
=======================
Binary file in odoo stored in file store or databse
to check option in configuration follow steps

system parameters

add follow ...........
key
ir_attachment.location
value
file

then it store binary file in filestore...........................!

our module can help us to get url of image store in filestore
steps to follow
you must install nginx for this ....



# first make filestore directory to public directly and only read rights for all, using nginx configuration
follow this article
https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/
server {
    root  /odoo/odoo-server/odoo-directory/filestore;
    location /db_name_directory {
   # db_name_directory its directory in odoo filestore which is named as per database name
    }
}

#next step change data directory in odoo
current data directory in odoo is in
~/.local/share/Odoo/filestore/
change it to outside .local folder anywhere on server
 like this /odoo/odoo-server/odoo-directory;

mentioned above change in odoo.conf file

data_dir = /odoo/odoo-server/odoo-directory

our code work to compute url of image it need some param like res_model,res_field,res_id