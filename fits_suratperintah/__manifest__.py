# -*- coding: utf-8 -*-
{
    'name': "Surat Perintah Kerja",

    'summary': """
        Addons HR untuk penerbitan Surat Perintah""",

    'description': """
        Addons HR untuk penerbitan Surat Perintah
    """,

    'author': "PT Fujicon Priangan Perdana",
    'website': "http://www.fujicon-japan.com",

    'category': 'HR',
    'version': '0.1.0',

    'depends': ['hr'],

    'data': [
        'security/ir.model.access.csv',
        'data/no_urut_surat.xml',
        'views/surat_perintah_kerja.xml',
        'report/print_suratjalan.xml',
    ],
    'installable': True,
}