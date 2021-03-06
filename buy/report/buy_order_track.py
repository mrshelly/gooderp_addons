# -*- coding: utf-8 -*-

from openerp import fields, models

class buy_order_track(models.TransientModel):
    _name = 'buy.order.track'
    _description = u'采购订单跟踪表'

    goods_code = fields.Char(u'商品编码')
    goods_id = fields.Many2one('goods', u'商品名称')
    attribute = fields.Char(u'属性')
    uom = fields.Char(u'单位')
    date = fields.Date(u'订单日期')
    order_name = fields.Char(u'采购订单编号')
    partner_id = fields.Many2one('partner', u'供应商')
    goods_state = fields.Char(u'状态')
    qty = fields.Float(u'数量')
    amount = fields.Float(u'采购额')  # 商品的价税合计
    qty_not_in = fields.Float(u'未入库数量')
    planned_date = fields.Date(u'要求交货日期')
    wh_in_date = fields.Date(u'入库日期')
    note = fields.Char(u'备注')
