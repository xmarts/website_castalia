# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import json
import logging
from werkzeug.exceptions import Forbidden, NotFound

from odoo import http, tools, _
from odoo.http import request
from odoo.addons.base.ir.ir_qweb.fields import nl2br
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.exceptions import ValidationError
from odoo.addons.website.controllers.main import Website
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.osv import expression

_logger = logging.getLogger(__name__)

PPG = 20  # Products Per Page
PPR = 4   # Products Per Row

class WebsiteCastalia(http.Controller):
	@http.route(['/shop/notas'], type='http', auth="public", website=True)
	def notas(self, **post):
		nota = http.request.env['account.invoice'].sudo().search([('type', '=', 'out_refund')])
		return http.request.render('website_castalia.index', {'nota':nota})
		#return request.redirect("/website_castalia/index")


	"""@http.route('/shop/notas/', auth='public')
	def index(self, **kw):
		 return http.request.render('website_castalia.index')"""

