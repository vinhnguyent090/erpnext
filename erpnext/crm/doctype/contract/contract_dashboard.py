from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'heatmap': False,
		'heatmap_message': _('This is based on transactions against this Contract. See timeline below for details'),
		'fieldname': 'contract',
		'non_standard_fieldnames': {
			'Coupons': 'reference_name',
			'Contract Repayment': 'against_contract',
			'Contract Interest Payment': 'against_contract',
		},
		'transactions': [
			{
				'label': _('Contract'),
				'items': ['Contract Loan','Contract Interest Payment','Contract Repayment']
			},
			{
				'label': _('Links'),
				'items': ['Payment Entry', 'Sales Invoice', 'Coupons']
			},
		]
	}
