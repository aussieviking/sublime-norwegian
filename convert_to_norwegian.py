import sublime, sublime_plugin

class NorwegianCommand(sublime_plugin.TextCommand):

	def convert_all(self, edit, old, new):
		cursor = 0
		for reg in self.view.find_all(old):
			theregion = sublime.Region(reg.begin() - cursor, reg.end() - cursor)
			self.view.replace(edit, theregion, new)
			cursor += 1

	def run(self, edit):
		self.convert_all(edit, 'Ae', u'\u00C6')
		self.convert_all(edit, 'ae', u'\u00E6')
		self.convert_all(edit, 'Oe', u'\u00D8')
		self.convert_all(edit, 'oe', u'\u00F8')
		self.convert_all(edit, 'Aa', u'\u00C5')
		self.convert_all(edit, 'aa', u'\u00E5')
		