from tree import Tree

class Organogram(Tree):
	def __init__(self, data: str, designation: str):
		super().__init__(data)
		self.designation = designation

	def print_tree(self, command: str):
		if command == "name":
			spaces = ' ' * self.get_level() * 3
			prefix = spaces + "|__" if self.parent else ""
			print(prefix + self.data)
			if self.children:
				for child in self.children:
					child.print_tree(command)

		if command == "designation":
			spaces = ' ' * self.get_level() * 3
			prefix = spaces + "|__" if self.parent else ""
			print(prefix + self.designation)
			if self.children:
				for child in self.children:
					child.print_tree(command)

		if command == "both":
			spaces = ' ' * self.get_level() * 3
			prefix = spaces + "|__" if self.parent else ""
			print(prefix + self.data + " (" + self.designation + ")")
			if self.children:
				for child in self.children:
					child.print_tree(command)


def main(command: str):
	organogram = Organogram('Sten', 'CEO')
	CTO = Organogram('Elon', 'CTO')
	InfrastructureHead = Organogram('Pichai', 'Infrastructure Head')
	CloudManager = Organogram('Jeff', 'Cloud Manager')
	AppManager = Organogram('Sam', "App Manager")
	ApplicationHead = Organogram('Mark', 'Application Head')
	HRHead = Organogram('Steve', 'HR Head')
	RecruitmentManager = Organogram('Theil', 'Recruitment Manager')
	PolicyManager = Organogram('Gensen', 'Policy Manager')

	organogram.add_child(CTO)
	organogram.add_child(HRHead)

	CTO.add_child(InfrastructureHead)
	CTO.add_child(ApplicationHead)
	InfrastructureHead.add_child(CloudManager)
	InfrastructureHead.add_child(AppManager)

	HRHead.add_child(RecruitmentManager)
	HRHead.add_child(PolicyManager)

	organogram.print_tree(command)

# main("both")
main("designation")
# main("name")