# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SuratPerintahKerja(models.Model):
    _name = 'surat.perintah.kerja'
    _inherit = 'hr.employee'

    tujuan_kegiatan = fields.Char(string='Tujuan Kegiatan', required=True)
    tempat = fields.Char(string='Tempat', required=True)
    hari_tanggal = fields.Char(string='Hari Tanggal', required=True)
    waktu = fields.Char(string='Waktu')
    employee_ids = fields.One2many('spk.user', 'surat_perintah_kerja_id', string='Employee', required=True)


class SpkUser(models.Model):
    _name = 'spk.user'

    employee_id = fields.Many2one('hr.employee', string='Karyawan')
    jabatan = fields.Char(related='employee_id.job_id.name', string='Jabatan')
    surat_perintah_kerja_id = fields.Many2one('surat.perintah.kerja', string='Surat Perintah Kerja')

