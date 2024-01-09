# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SuratPerintahKerja(models.Model):
    _name = 'surat.perintah.kerja'
    _description = "Surat Perintah Kerja"
    _rec_name = "tujuan_kegiatan"
    _inherit = ['mail.thread']

    tujuan_kegiatan = fields.Char(string='Tujuan Kegiatan', required=True)
    tempat = fields.Char(string='Tempat', required=True)
    hari_tanggal = fields.Char(string='Hari Tanggal', required=True)
    waktu = fields.Char(string='Waktu', required=True)
    ttd = fields.Many2one('hr.employee',string="Penanda Tangan SPK", required=True)
    spk_user_ids = fields.One2many('spk.user', 'surat_perintah_kerja_id', string='Employee')
    tgl_ttd = fields.Char(string="Tgl TTD SPK")
    tahun_surat = fields.Char(string="Tahun Surat", required=True)
    bulan_surat = fields.Selection([('I', 'I'),('II', 'II'),('III', 'III')
                                       ,('IV', 'IV'),('V', 'V'),('VI', 'VI')
                                       ,('VII', 'VII'),('VIII', 'VIII'),('IX', 'IX')
                                       , ('X', 'X'),('XI', 'XI'),('XII', 'XII')
                                    ],string="Bulan Surat", required=True)
    no_urut_surat = fields.Char(string="No Urut Surat", readonly=True, required=True, copy=False, default='New')
    lampiran_ttd = fields.Binary('Lampiran TTD SPK')
    filename_ttd = fields.Char('Nama Lampiran TTD SM')

    @api.model
    def create(self, vals):
        if vals.get('no_urut_surat', 'New') == 'New':
            vals['no_urut_surat'] = self.env['ir.sequence'].next_by_code('no.urut.surat') or 'New'
        result = super(SuratPerintahKerja, self).create(vals)
        return result



class SpkUser(models.Model):
    _name = 'spk.user'
    _description = "Personil Penugasan"

    surat_perintah_kerja_id = fields.Many2one('surat.perintah.kerja', string='Surat Perintah Kerja')
    employee_id = fields.Many2one('hr.employee', string='Nama')
    nik = fields.Char(string="NIK", required=True)
    jabatan = fields.Char(related='employee_id.job_id.name', string='Jabatan', store=True, readonly=True)



