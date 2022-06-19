from frappe import _


def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on the attendance of this Employee'),
		'fieldname': 'employee',
		'non_standard_fieldnames': {
			'Asset': 'custodian',
			'ToDo': 'reference_name',
			'Bank Account': 'party',
			'Employee Grievance': 'raised_by',
			'Journal Entry': 'party'
		},
		'transactions': [
			{
				"label": _("Leave"),
				"items": ["Leave Application", "Leave Allocation", "Leave Policy Assignment"],
			},
			{
				"label": _("Lifecycle"),
				"items": [
					"Employee Transfer",
					"Employee Promotion",
					"Employee Separation",
					"Employee Grievance",
				],
			},
			{"label": _("Shift"), "items": ["Shift Request", "Shift Assignment"]},
			{"label": _("Expense"), "items": ["Expense Claim", "Travel Request", "Employee Advance"]},
			{"label": _("Benefit"), "items": ["Employee Benefit Application", "Employee Benefit Claim"]},
			{
				"label": _("Payroll"),
				"items": [
					"Salary Structure Assignment",
					"Salary Slip",
					"Additional Salary",
					"Timesheet",
					"Employee Incentive",
					"Retention Bonus",
					"Bank Account",
				],
			},
			{
				"label": _("Training"),
				"items": ["Training Event", "Training Result", "Training Feedback", "Employee Skill Map"],
			},
			{
				'label': _('Expense'),
				'items': ['Expense Claim', 'Travel Request', 'Employee Advance', 'Journal Entry']
			},
			{
				'label': _('Benefit'),
				'items': ['Employee Benefit Application', 'Employee Benefit Claim']
			},
			{
				'label': _('Payroll'),
				'items': ['Salary Structure Assignment', 'Salary Slip', 'Additional Salary', 'Timesheet','Employee Incentive', 'Retention Bonus', 'Bank Account']
			},
			{
				'label': _('Training'),
				'items': ['Training Event', 'Training Result', 'Training Feedback', 'Employee Skill Map', 'ToDo']
			},
			{
				'label': _('Evaluation'),
				'items': ['Appraisal']
			},
				{
				'label': _('Asset'),
				'items': ['Asset']
			},
			{"label": _("Evaluation"), "items": ["Appraisal"]},
		],
	}
