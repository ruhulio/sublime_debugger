from __future__ import annotations
from ..typecheck import *

if TYPE_CHECKING:
	from . html import element

class Layout:
	def dirty(self) -> None:
		...
	def remove_component_children(self, item: 'element') -> None:
		...
	def remove_component(self, item: 'element') -> None:
		...
	def add_component_children(self, item: 'element') -> None:
		...
	def add_component(self, item: 'element') -> None:
		...
	def render_component_tree(self, item: 'element') -> None:
		...
	def render_component(self, item: 'element') -> None:
		...
	def render(self) -> bool:
		...
	def dispose(self) -> None:
		...
	def rem_width_scale(self) -> float:
		...
	def width(self) -> float:
		...
	def height(self) -> float:
		...
	def luminocity(self) -> float:
		...
	def on_navigate(self, path: str) -> None:
		...
	def register_on_click_handler(self, callback: 'Callable') -> str:
		...
