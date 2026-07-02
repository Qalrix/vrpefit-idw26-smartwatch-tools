# This Python file uses the following encoding: utf-8
import sys
import os
import json
import copy
import math
import shutil
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFileDialog, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QSplitter, QScrollArea, QFrame, QSlider,
    QGroupBox, QGridLayout, QMessageBox, QDialog, QTextEdit,
    QListWidget, QListWidgetItem, QLineEdit, QComboBox,
    QStackedWidget, QSizePolicy, QSpacerItem, QInputDialog,
    QMenu, QStatusBar, QToolBar, QDockWidget
)
from PySide6.QtCore import (
    Qt, QSize, QTimer, QTime, QPoint, QRect, QRectF,
    Signal, Slot, QThread, QPropertyAnimation, QEasingCurve,
    QEvent, QFileInfo
)
from PySide6.QtGui import (
    QPixmap, QPainter, QPen, QColor, QBrush, QFont, QFontDatabase,
    QIcon, QTransform, QImage, QPalette, QAction, QKeySequence,
    QLinearGradient, QRadialGradient, QPainterPath, QCursor
)

from ui_main import Ui_MainWindow
import rc_resources  # This is the compiled resource file (from resources.qrc)

# ─────────────────────────────────────────────
#  STYLESHEET
# ─────────────────────────────────────────────
DARK_CYAN_STYLESHEET = """
QMainWindow, QDialog, QWidget {
    background-color: #0d1117;
    color: #c9d1d9;
    font-size: 13px;
}

/* ── Toolbar ── */
QToolBar {
    background-color: #161b22;
    border-bottom: 1px solid #21262d;
    spacing: 4px;
    padding: 4px 8px;
}
QToolBar QToolButton {
    background-color: transparent;
    color: #8b949e;
    border: 1px solid transparent;
    border-radius: 5px;
    padding: 5px 10px;
    font-size: 12px;
}
QToolBar QToolButton:hover {
    background-color: #1f6b75;
    color: #e6edf3;
    border-color: #00bcd4;
}
QToolBar QToolButton:pressed {
    background-color: #0097a7;
}

/* ── MenuBar ── */
QMenuBar {
    background-color: #161b22;
    color: #c9d1d9;
    border-bottom: 1px solid #21262d;
    padding: 2px;
}
QMenuBar::item:selected {
    background-color: #1f6b75;
    color: #e6edf3;
    border-radius: 4px;
}
QMenu {
    background-color: #1c2128;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 4px;
}
QMenu::item:selected {
    background-color: #1f6b75;
    color: #e6edf3;
    border-radius: 4px;
}
QMenu::separator {
    height: 1px;
    background: #30363d;
    margin: 4px 8px;
}

/* ── Buttons ── */
QPushButton {
    background-color: #1c2128;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 1px 2px;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #1f6b75;
    color: #e6edf3;
    border-color: #00bcd4;
}
QPushButton:pressed {
    background-color: #006064;
    border-color: #00acc1;
}
QPushButton#primaryBtn {
    background-color: #006064;
    color: #e6edf3;
    border-color: #00bcd4;
    font-weight: bold;
}
QPushButton#primaryBtn:hover {
    background-color: #00838f;
}
QPushButton#dangerBtn {
    background-color: #3d1a1a;
    color: #ff8080;
    border-color: #c62828;
}
QPushButton#dangerBtn:hover {
    background-color: #c62828;
    color: #ffffff;
}
QPushButton#successBtn {
    background-color: #1a3d2b;
    color: #69db7c;
    border-color: #2ea043;
}
QPushButton#successBtn:hover {
    background-color: #2ea043;
    color: #ffffff;
}

/* ── GroupBox ── */
QGroupBox {
    border: 1px solid #21262d;
    border-radius: 8px;
    margin-top: 14px;
    padding-top: 8px;
    color: #8b949e;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 6px;
    color: #00bcd4;
}

/* ── TabWidget ── */
QTabWidget::pane {
    border: 1px solid #21262d;
    border-radius: 6px;
    background-color: #0d1117;
}
QTabBar::tab {
    background-color: #1c2128;
    color: #8b949e;
    border: 1px solid #30363d;
    border-bottom: none;
    border-radius: 6px 6px 0 0;
    padding: 7px 16px;
    margin-right: 2px;
    font-size: 12px;
}
QTabBar::tab:selected {
    background-color: #0d1117;
    color: #00bcd4;
    border-color: #30363d;
    border-bottom: 2px solid #00bcd4;
}
QTabBar::tab:hover:!selected {
    background-color: #1f6b75;
    color: #e6edf3;
}

/* ── TreeWidget ── */
QTreeWidget {
    background-color: #0d1117;
    color: #c9d1d9;
    border: 1px solid #21262d;
    border-radius: 6px;
    alternate-background-color: #161b22;
}
QTreeWidget::item {
    padding: 3px 0;
    border-radius: 3px;
}
QTreeWidget::item:selected {
    background-color: #1f3a4a;
    color: #00e5ff;
}
QTreeWidget::item:hover {
    background-color: #1c2f3a;
}
QHeaderView::section {
    background-color: #161b22;
    color: #8b949e;
    border: none;
    border-right: 1px solid #21262d;
    border-bottom: 1px solid #21262d;
    padding: 5px 8px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 0.5px;
}

/* ── ListWidget ── */
QListWidget {
    background-color: #0d1117;
    color: #c9d1d9;
    border: 1px solid #21262d;
    border-radius: 6px;
    outline: none;
}
QListWidget::item {
    padding: 6px 10px;
    border-radius: 4px;
}
QListWidget::item:selected {
    background-color: #1f3a4a;
    color: #00e5ff;
}
QListWidget::item:hover {
    background-color: #1c2f3a;
}

/* ── ScrollBar ── */
QScrollBar:vertical {
    background: #0d1117;
    width: 10px;
    border-radius: 5px;
}
QScrollBar::handle:vertical {
    background: #30363d;
    border-radius: 5px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background: #00bcd4;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}
QScrollBar:horizontal {
    background: #0d1117;
    height: 10px;
    border-radius: 5px;
}
QScrollBar::handle:horizontal {
    background: #30363d;
    border-radius: 5px;
    min-width: 20px;
}
QScrollBar::handle:horizontal:hover {
    background: #00bcd4;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

/* ── Slider ── */
QSlider::groove:horizontal {
    height: 4px;
    background: #21262d;
    border-radius: 2px;
}
QSlider::handle:horizontal {
    background: #00bcd4;
    border: 2px solid #006064;
    width: 16px;
    height: 16px;
    margin: -6px 0;
    border-radius: 8px;
}
QSlider::handle:horizontal:hover {
    background: #00e5ff;
    border-color: #00838f;
}
QSlider::sub-page:horizontal {
    background: #006064;
    border-radius: 2px;
}

/* ── LineEdit / TextEdit ── */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #0d1117;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 5px 8px;
    selection-background-color: #1f3a4a;
}
QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border-color: #00bcd4;
}

/* ── ComboBox ── */
QComboBox {
    background-color: #1c2128;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 4px 8px;
}
QComboBox:hover {
    border-color: #00bcd4;
}
QComboBox::drop-down {
    border: none;
    width: 20px;
}
QComboBox QAbstractItemView {
    background-color: #1c2128;
    color: #c9d1d9;
    border: 1px solid #30363d;
    selection-background-color: #1f3a4a;
}

/* ── StatusBar ── */
QStatusBar {
    background-color: #006064;
    color: #e6edf3;
    font-size: 11px;
    border-top: 1px solid #00838f;
}
QStatusBar QLabel {
    padding: 0 6px;
    color: #e6edf3;
}

/* ── Splitter ── */
QSplitter::handle {
    background-color: #21262d;
    width: 3px;
    height: 3px;
}
QSplitter::handle:hover {
    background-color: #00bcd4;
}

/* ── Frame ── */
QFrame[frameShape="4"], QFrame[frameShape="5"] {
    color: #21262d;
}

/* ── DockWidget ── */
QDockWidget {
    color: #c9d1d9;
    titlebar-close-icon: none;
}
QDockWidget::title {
    background-color: #161b22;
    border-bottom: 1px solid #21262d;
    padding: 6px 10px;
    color: #00bcd4;
    font-weight: bold;
    letter-spacing: 0.5px;
}

/* ── Tooltip ── */
QToolTip {
    background-color: #161b22;
    color: #c9d1d9;
    border: 1px solid #00bcd4;
    border-radius: 4px;
    padding: 4px 8px;
    font-size: 11px;
}
"""


# ─────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────
CANVAS_W = 240
CANVAS_H = 284
PREVIEW_W = 174
PREVIEW_H = 196

SKELETON_IWF = {
    "version": 1,
    "clouddialversion": 3,
    "preview": "preview.bmp",
    "name": "custom",
    "author": "authorname",
    "description": "custom",
    "bkground": "image.bmp",
    "item": []
}

DEFAULT_WATCH_ITEM = {
    "widget": "watch",
    "type": "time",
    "x": 0,
    "y": 0,
    "w": 240,
    "h": 284,
    "hour": "",
    "minute": "",
    "second": "",
    "hourcenterx": 0,
    "hourcentery": 0,
    "mincenterx": 0,
    "mincentery": 0,
    "seccenterx": 0,
    "seccentery": 0,
    "houranchorx": 120,
    "houranchory": 142,
    "minanchorx": 120,
    "minanchory": 142,
    "secanchorx": 120,
    "secanchory": 142
}


# ─────────────────────────────────────────────
#  CANVAS PREVIEW WIDGET
# ─────────────────────────────────────────────
class CanvasPreview(QWidget):
    """Renders a 240×284 watch face canvas with background + hands."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(CANVAS_W, CANVAS_H)
        self._bg_pixmap: QPixmap | None = None
        self._hour_pixmap: QPixmap | None = None
        self._min_pixmap: QPixmap | None = None
        self._sec_pixmap: QPixmap | None = None

        self._hour_angle = 0.0
        self._min_angle  = 0.0
        self._sec_angle  = 0.0

        self._hand_centers = {
            "hour": QPoint(0, 0),
            "minute": QPoint(0, 0),
            "second": QPoint(0, 0)
        }
        self._hand_anchors = {
            "hour": QPoint(CANVAS_W // 2, CANVAS_H // 2),
            "minute": QPoint(CANVAS_W // 2, CANVAS_H // 2),
            "second": QPoint(CANVAS_W // 2, CANVAS_H // 2)
        }
        self.setCursor(Qt.CrossCursor)

    def set_background(self, pixmap: QPixmap | None):
        self._bg_pixmap = pixmap
        self.update()

    def set_hand(self, hand: str, pixmap: QPixmap | None):
        if hand == "hour":
            self._hour_pixmap = pixmap
        elif hand == "minute":
            self._min_pixmap = pixmap
        elif hand == "second":
            self._sec_pixmap = pixmap
        self.update()

    def set_angles(self, hour_deg: float, min_deg: float, sec_deg: float):
        self._hour_angle = hour_deg
        self._min_angle  = min_deg
        self._sec_angle  = sec_deg
        self.update()

    def set_hand_coords(self, hand: str, center_x: int, center_y: int,
                       anchor_x: int, anchor_y: int):
        self._hand_centers[hand] = QPoint(center_x, center_y)
        self._hand_anchors[hand] = QPoint(anchor_x, anchor_y)
        self.update()

    def _draw_hand(self, painter: QPainter, hand: str, pixmap: QPixmap, angle: float):
        """Draw a hand rotated around the configured image pivot and anchor."""
        if pixmap is None:
            return
        center = self._hand_centers.get(hand, QPoint(pixmap.width() // 2,
                                                      pixmap.height() // 2))
        anchor = self._hand_anchors.get(hand, QPoint(CANVAS_W // 2, CANVAS_H // 2))
        painter.save()
        painter.translate(anchor)
        painter.rotate(angle)
        painter.translate(-center)
        painter.drawPixmap(0, 0, pixmap)
        painter.restore()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        # Background
        if self._bg_pixmap:
            scaled = self._bg_pixmap.scaled(CANVAS_W, CANVAS_H,
                                            Qt.KeepAspectRatioByExpanding,
                                            Qt.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled)
        else:
            # Checkerboard placeholder
            checker_size = 20
            for row in range(CANVAS_H // checker_size + 1):
                for col in range(CANVAS_W // checker_size + 1):
                    color = QColor("#1a1a2e") if (row + col) % 2 == 0 else QColor("#16213e")
                    painter.fillRect(col * checker_size, row * checker_size,
                                     checker_size, checker_size, color)
            # Label
            painter.setPen(QColor("#30363d"))
            painter.setFont(QFont("Segoe UI", 10))
            painter.drawText(self.rect(), Qt.AlignCenter, "No Background\n240 × 284")

        # Clock hands
        self._draw_hand(painter, "hour", self._hour_pixmap, self._hour_angle)
        self._draw_hand(painter, "minute", self._min_pixmap, self._min_angle)
        self._draw_hand(painter, "second", self._sec_pixmap, self._sec_angle)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize data
        self._iwf_data: dict = copy.deepcopy(SKELETON_IWF)
        self._bg_path: str | None = None
        self._hand_filenames: dict[str, str] = {}
        self._resources: dict[str, QPixmap] = {}

        # Setup custom canvas (replace the graphicsView in the UI)
        self._setup_canvas()

        # Setup connections
        self._setup_connections()

        # Setup resource list
        self._setup_resource_list()

        # Setup clock hands panel connections
        self._setup_clock_hands_panel()

        # Setup rotation panel connections
        self._setup_rotation_panel()

        # Update status bar
        self.ui.statusbar.showMessage("Ready")

        # Update JSON tree with initial data
        self._update_json_tree()

        # Initialize spinboxes with default values
        self._init_spinboxes()

    def _setup_canvas(self):
        """Replace the graphicsView with our custom CanvasPreview"""
        # Create canvas widget
        self.canvas = CanvasPreview()

        # Find the graphicsView in the UI and replace it
        # The graphicsView is in groupBox (preview container)
        if hasattr(self.ui, 'graphicsView'):
            # Get the parent layout
            parent_layout = self.ui.graphicsView.parent().layout()
            if parent_layout:
                # Find the index of graphicsView
                for i in range(parent_layout.count()):
                    widget = parent_layout.itemAt(i).widget()
                    if widget == self.ui.graphicsView:
                        parent_layout.removeWidget(self.ui.graphicsView)
                        parent_layout.insertWidget(i, self.canvas)
                        break
            self.ui.graphicsView.hide()
            self.ui.graphicsView.deleteLater()

    def _setup_connections(self):
        """Setup all UI connections"""
        # Menu actions
        self.ui.actionNew_Dial.triggered.connect(self._new_dial)
        self.ui.actionOpen_Folder.triggered.connect(self._open_project)
        self.ui.actionSave_iwf_json.triggered.connect(self._save_iwf)
        self.ui.actionSave_font_json.triggered.connect(self._save_font_json)  # Stub
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionValidate_iwf_json.triggered.connect(lambda: self._validate(json_only=True))
        self.ui.actionValidate_font_json.triggered.connect(self._validate_font_json)  # Stub
        self.ui.actionValidate_structure.triggered.connect(lambda: self._validate(json_only=False))
        self.ui.actionAbout.triggered.connect(self._show_about)

        # Background buttons
        self.ui.pushButtonUploadBkg.clicked.connect(self._upload_background)
        self.ui.pushButtonClearBkg.clicked.connect(self._clear_background)

        # Resource viewer buttons
        self.ui.pushButtonAddFile.clicked.connect(self._add_resource)
        self.ui.pushButtonRemoveFile.clicked.connect(self._remove_resource)
        self.ui.listWidget.currentRowChanged.connect(self._on_resource_selected_changed)

        # Clock hand load/clear buttons
        self.ui.pushButtonLoadResHour.clicked.connect(lambda: self._load_hand("hour"))
        self.ui.pushButtonClearResHour.clicked.connect(lambda: self._clear_hand("hour"))
        self.ui.pushButtonLoadResMin.clicked.connect(lambda: self._load_hand("minute"))
        self.ui.pushButtonClearResMin.clicked.connect(lambda: self._clear_hand("minute"))
        self.ui.pushButtonLoadResSec.clicked.connect(lambda: self._load_hand("second"))
        self.ui.pushButtonClearResSec.clicked.connect(lambda: self._clear_hand("second"))

        # Spinbox connections for center/anchor values
        self.ui.spinBoxHourCenterX.valueChanged.connect(lambda: self._on_spinbox_changed("hour"))
        self.ui.spinBoxHourCenterY.valueChanged.connect(lambda: self._on_spinbox_changed("hour"))
        self.ui.spinBoxHourAnchorX.valueChanged.connect(lambda: self._on_spinbox_changed("hour"))
        self.ui.spinBoxHourAnchorY.valueChanged.connect(lambda: self._on_spinbox_changed("hour"))

        self.ui.spinBoxMinCenterX.valueChanged.connect(lambda: self._on_spinbox_changed("minute"))
        self.ui.spinBoxMinCenterY.valueChanged.connect(lambda: self._on_spinbox_changed("minute"))
        self.ui.spinBoxMinAnchorX.valueChanged.connect(lambda: self._on_spinbox_changed("minute"))
        self.ui.spinBoxMinAnchorY.valueChanged.connect(lambda: self._on_spinbox_changed("minute"))

        self.ui.spinBoxSecCenterX.valueChanged.connect(lambda: self._on_spinbox_changed("second"))
        self.ui.spinBoxSecCenterY.valueChanged.connect(lambda: self._on_spinbox_changed("second"))
        self.ui.spinBoxSecAnchorX.valueChanged.connect(lambda: self._on_spinbox_changed("second"))
        self.ui.spinBoxSecAnchorY.valueChanged.connect(lambda: self._on_spinbox_changed("second"))

        # Rotation sliders
        self.ui.horizontalSliderHourRotation.valueChanged.connect(self._on_rotation_changed)
        self.ui.horizontalSliderMinRotation.valueChanged.connect(self._on_rotation_changed)
        self.ui.horizontalSliderSecRotation.valueChanged.connect(self._on_rotation_changed)
        self.ui.pushButtonResetRotations.clicked.connect(self._reset_rotations)

        # JSON tree buttons
        self.ui.pushButtonExpandAll.clicked.connect(self.ui.treeWidget.expandAll)
        self.ui.pushButtonCollapseAll.clicked.connect(self.ui.treeWidget.collapseAll)
        self.ui.pushButtonRawIwfJson.clicked.connect(self._show_raw_json)

        # Export buttons (stubs for now)
        self.ui.pushButtonExportIwf.clicked.connect(self._export_iwf_stub)
        self.ui.pushButtonExportIwfLz.clicked.connect(self._export_iwf_lz_stub)
        self.ui.pushButtonExportEntireDial.clicked.connect(self._export_entire_dial_stub)

        # Export buttons (Preview button)
        self.ui.actionExport_Preview.triggered.connect(self._export_preview)

    def _export_preview(self):
        if not self._bg_path:
            QMessageBox.warning(self, "No Background",
                "Please upload a background image before exporting a preview.")
            return

        save_path, _ = QFileDialog.getSaveFileName(
            self, "Export Preview Image", "preview.png",
            "PNG Image (*.png);;All Files (*)"
        )
        if save_path:
            # 1. Render the canvas to a pixmap
            preview_pixmap = QPixmap(self.canvas.size())
            self.canvas.render(preview_pixmap)

            # 2. Scale to the required dimensions
            scaled_preview = preview_pixmap.scaled(
                165,
                196,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            # 3. Use QFileInfo to check the Qt Resource path
            border_path = ":/images/border.png"
            if QFileInfo(border_path).exists():
                border_pixmap = QPixmap(border_path)
                border_pixmap = border_pixmap.scaled(PREVIEW_W, PREVIEW_H)

                # Create destination image
                final_pixmap = QPixmap(PREVIEW_W, PREVIEW_H)
                final_pixmap.fill(Qt.black)

                # Create painter ONLY after the target pixmap exists
                painter = QPainter(final_pixmap)
                painter.setRenderHint(QPainter.Antialiasing)
                painter.setRenderHint(QPainter.SmoothPixmapTransform)

                # Calculate centered position
                x = (PREVIEW_W - scaled_preview.width()) // 2
                y = (PREVIEW_H - scaled_preview.height()) // 2

                # Draw centered preview
                painter.drawPixmap(x, y, scaled_preview)

                # Draw border on top
                painter.drawPixmap(0, 0, border_pixmap)

                painter.end()

                # Save the final image
                final_pixmap.save(save_path)
                QMessageBox.information(self, "Export Successful", f"Preview exported to:\n{save_path}")
            else:
                QMessageBox.warning(self, "Border Image Missing",
                    "Border image not found. Please ensure 'images/border.png' exists in the resource file.")

    def _setup_resource_list(self):
        """Initialize the resource list widget"""
        self.ui.listWidget.setIconSize(QSize(48, 48))
        self.ui.label_2.setText("Select a resource to preview")

    def _setup_clock_hands_panel(self):
        """Setup clock hands panel labels and info"""
        # Set initial text for background label
        self.ui.label.setText("No background uploaded")

        # Set initial center/anchor values from defaults
        self.ui.spinBoxHourCenterX.setValue(0)
        self.ui.spinBoxHourCenterY.setValue(0)
        self.ui.spinBoxHourAnchorX.setValue(120)
        self.ui.spinBoxHourAnchorY.setValue(142)

        self.ui.spinBoxMinCenterX.setValue(0)
        self.ui.spinBoxMinCenterY.setValue(0)
        self.ui.spinBoxMinAnchorX.setValue(120)
        self.ui.spinBoxMinAnchorY.setValue(142)

        self.ui.spinBoxSecCenterX.setValue(0)
        self.ui.spinBoxSecCenterY.setValue(0)
        self.ui.spinBoxSecAnchorX.setValue(120)
        self.ui.spinBoxSecAnchorY.setValue(142)

        # Initialize rotation labels
        self.ui.label_20.setText("Hour (Angle: 0°)")
        self.ui.label_21.setText("Minute (Angle: 0°)")
        self.ui.label_22.setText("Second (Angle: 0°)")

        # Set slider ranges
        self.ui.horizontalSliderHourRotation.setRange(0, 360)
        self.ui.horizontalSliderMinRotation.setRange(0, 360)
        self.ui.horizontalSliderSecRotation.setRange(0, 360)

        self.ui.horizontalSliderHourRotation.setValue(0)
        self.ui.horizontalSliderMinRotation.setValue(0)
        self.ui.horizontalSliderSecRotation.setValue(0)

    def _setup_rotation_panel(self):
        """Setup rotation panel connections"""
        pass  # Already connected in _setup_connections

    def _init_spinboxes(self):
        """Initialize spinboxes with proper ranges"""
        for spinbox in [self.ui.spinBoxHourCenterX, self.ui.spinBoxHourCenterY,
                        self.ui.spinBoxMinCenterX, self.ui.spinBoxMinCenterY,
                        self.ui.spinBoxSecCenterX, self.ui.spinBoxSecCenterY,
                        self.ui.spinBoxHourAnchorX, self.ui.spinBoxHourAnchorY,
                        self.ui.spinBoxMinAnchorX, self.ui.spinBoxMinAnchorY,
                        self.ui.spinBoxSecAnchorX, self.ui.spinBoxSecAnchorY]:
            spinbox.setRange(0, 999)

    # ── Resource Management ────────────────────────────────────────────────

    def _add_resource(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Add Resource Files", "",
            "Images (*.bmp *.png *.jpg *.jpeg);;All Files (*)"
        )
        for f in files:
            self._add_file_to_resources(f)

    def _add_file_to_resources(self, path: str):
        name = os.path.basename(path)
        if name in self._resources:
            return
        pix = QPixmap(path)
        if pix.isNull():
            return
        self._resources[name] = pix
        icon = QIcon(pix.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        item = QListWidgetItem(icon, name)
        item.setData(Qt.UserRole, path)
        self.ui.listWidget.addItem(item)
        self.ui.statusbar.showMessage(f"Added: {name}")

    def _remove_resource(self):
        row = self.ui.listWidget.currentRow()
        if row < 0:
            return
        item = self.ui.listWidget.item(row)
        name = item.text()
        del self._resources[name]
        self.ui.listWidget.takeItem(row)
        self.ui.label_2.setText("Select a resource to preview")
        self.ui.statusbar.showMessage(f"Removed: {name}")

    def _on_resource_selected_changed(self, row: int):
        if row < 0:
            return
        item = self.ui.listWidget.item(row)
        name = item.text()
        pix = self._resources.get(name)
        if pix:
            scaled = pix.scaled(116, 116, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.label_2.setPixmap(scaled)

    def _get_pixmap(self, name: str) -> QPixmap | None:
        return self._resources.get(name)

    def _get_all_resource_names(self) -> list[str]:
        return list(self._resources.keys())

    # ── Hand Loading ───────────────────────────────────────────────────────

    def _load_hand(self, hand: str):
        names = self._get_all_resource_names()
        if not names:
            QMessageBox.information(self, "No Resources",
                "Please add image files to the Resource Viewer first.")
            return
        name, ok = QInputDialog.getItem(self, f"Select {hand} hand image",
                                        "Choose from resources:", names, 0, False)
        if ok and name:
            pix = self._get_pixmap(name)
            if pix:
                self.canvas.set_hand(hand, pix)
                self._hand_filenames[hand] = name

                # Auto-update center from image dimensions
                center_x = pix.width() // 2
                center_y = pix.height() // 2

                # Update appropriate spinboxes
                if hand == "hour":
                    self.ui.spinBoxHourCenterX.setValue(center_x)
                    self.ui.spinBoxHourCenterY.setValue(center_y)
                    # Update thumb display (using graphicsView as thumb placeholder)
                    self._update_hand_thumb("hour", pix)
                elif hand == "minute":
                    self.ui.spinBoxMinCenterX.setValue(center_x)
                    self.ui.spinBoxMinCenterY.setValue(center_y)
                    self._update_hand_thumb("minute", pix)
                elif hand == "second":
                    self.ui.spinBoxSecCenterX.setValue(center_x)
                    self.ui.spinBoxSecCenterY.setValue(center_y)
                    self._update_hand_thumb("second", pix)

                self._sync_hands_to_iwf()
                self._update_json_tree()
                self.ui.statusbar.showMessage(f"Loaded {hand} hand: {name}")

    def _update_hand_thumb(self, hand: str, pixmap: QPixmap):
        """Update the small thumb icon for the hand (using graphicsView placeholders)"""
        # The UI has graphicsView_2, graphicsView_4, graphicsView_5 as thumb placeholders
        thumb_map = {
            "hour": self.ui.graphicsView_2,
            "minute": self.ui.graphicsView_4,
            "second": self.ui.graphicsView_5
        }
        if hand in thumb_map:
            # Create a QPixmap for the thumb
            thumb = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # Since graphicsView is used, we'll just set a scene
            scene = thumb_map[hand].scene()
            if scene is None:
                from PySide6.QtWidgets import QGraphicsScene
                scene = QGraphicsScene()
                thumb_map[hand].setScene(scene)
            scene.clear()
            scene.addPixmap(thumb)
            thumb_map[hand].fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)

    def _clear_hand(self, hand: str):
        self.canvas.set_hand(hand, None)
        if hand in self._hand_filenames:
            del self._hand_filenames[hand]

        # Clear thumb
        thumb_map = {
            "hour": self.ui.graphicsView_2,
            "minute": self.ui.graphicsView_4,
            "second": self.ui.graphicsView_5
        }
        if hand in thumb_map and thumb_map[hand].scene():
            thumb_map[hand].scene().clear()

        # Reset center values to 0
        if hand == "hour":
            self.ui.spinBoxHourCenterX.setValue(0)
            self.ui.spinBoxHourCenterY.setValue(0)
        elif hand == "minute":
            self.ui.spinBoxMinCenterX.setValue(0)
            self.ui.spinBoxMinCenterY.setValue(0)
        elif hand == "second":
            self.ui.spinBoxSecCenterX.setValue(0)
            self.ui.spinBoxSecCenterY.setValue(0)

        self._sync_hands_to_iwf()
        self._update_json_tree()
        self.ui.statusbar.showMessage(f"Cleared {hand} hand")

    def _on_spinbox_changed(self, hand: str):
        """Called when center/anchor spinboxes change"""
        self._update_canvas_coords()
        self._sync_hands_to_iwf()
        self._update_json_tree()

    def _update_canvas_coords(self):
        """Update canvas with current center/anchor values"""
        # Hour
        self.canvas.set_hand_coords(
            "hour",
            self.ui.spinBoxHourCenterX.value(),
            self.ui.spinBoxHourCenterY.value(),
            self.ui.spinBoxHourAnchorX.value(),
            self.ui.spinBoxHourAnchorY.value()
        )
        # Minute
        self.canvas.set_hand_coords(
            "minute",
            self.ui.spinBoxMinCenterX.value(),
            self.ui.spinBoxMinCenterY.value(),
            self.ui.spinBoxMinAnchorX.value(),
            self.ui.spinBoxMinAnchorY.value()
        )
        # Second
        self.canvas.set_hand_coords(
            "second",
            self.ui.spinBoxSecCenterX.value(),
            self.ui.spinBoxSecCenterY.value(),
            self.ui.spinBoxSecAnchorX.value(),
            self.ui.spinBoxSecAnchorY.value()
        )

    def _sync_hands_to_iwf(self):
        """Ensure the watch item exists in iwf if any hand is assigned."""
        has_hands = len(self._hand_filenames) > 0
        items = self._iwf_data.get("item", [])

        # Find existing watch item
        watch_idx = next((i for i, it in enumerate(items)
                          if it.get("widget") == "watch"), None)

        if has_hands:
            if watch_idx is None:
                # Add default watch item
                items.append(copy.deepcopy(DEFAULT_WATCH_ITEM))
                watch_idx = len(items) - 1
            wi = items[watch_idx]
            # Update hand filenames
            wi["hour"] = self._hand_filenames.get("hour", "")
            wi["minute"] = self._hand_filenames.get("minute", "")
            wi["second"] = self._hand_filenames.get("second", "")
            # Update center/anchor values
            wi["hourcenterx"] = self.ui.spinBoxHourCenterX.value()
            wi["hourcentery"] = self.ui.spinBoxHourCenterY.value()
            wi["mincenterx"] = self.ui.spinBoxMinCenterX.value()
            wi["mincentery"] = self.ui.spinBoxMinCenterY.value()
            wi["seccenterx"] = self.ui.spinBoxSecCenterX.value()
            wi["seccentery"] = self.ui.spinBoxSecCenterY.value()
            wi["houranchorx"] = self.ui.spinBoxHourAnchorX.value()
            wi["houranchory"] = self.ui.spinBoxHourAnchorY.value()
            wi["minanchorx"] = self.ui.spinBoxMinAnchorX.value()
            wi["minanchory"] = self.ui.spinBoxMinAnchorY.value()
            wi["secanchorx"] = self.ui.spinBoxSecAnchorX.value()
            wi["secanchory"] = self.ui.spinBoxSecAnchorY.value()
        else:
            # Remove watch item if no hands
            if watch_idx is not None:
                items.pop(watch_idx)

        self._iwf_data["item"] = items

    # ── Rotation ───────────────────────────────────────────────────────────

    def _on_rotation_changed(self):
        hour_angle = self.ui.horizontalSliderHourRotation.value()
        min_angle = self.ui.horizontalSliderMinRotation.value()
        sec_angle = self.ui.horizontalSliderSecRotation.value()

        self.canvas.set_angles(hour_angle, min_angle, sec_angle)

        # Update labels
        self.ui.label_20.setText(f"Hour (Angle: {hour_angle}°)")
        self.ui.label_21.setText(f"Minute (Angle: {min_angle}°)")
        self.ui.label_22.setText(f"Second (Angle: {sec_angle}°)")

        self.ui.statusbar.showMessage(f"Rotation - H: {hour_angle}°  M: {min_angle}°  S: {sec_angle}°")

    def _reset_rotations(self):
        self.ui.horizontalSliderHourRotation.setValue(0)
        self.ui.horizontalSliderMinRotation.setValue(0)
        self.ui.horizontalSliderSecRotation.setValue(0)
        self.canvas.set_angles(0, 0, 0)
        self.ui.statusbar.showMessage("Rotations reset to 12:00:00")

    # ── Background ─────────────────────────────────────────────────────────

    def _upload_background(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Upload Background",
            "", "BMP Files (*.bmp)"
        )
        if not path:
            return
        pix = QPixmap(path)
        if pix.isNull():
            QMessageBox.warning(self, "Invalid Image", "Could not load the selected file.")
            return
        if pix.width() > CANVAS_W or pix.height() > CANVAS_H:
            QMessageBox.information(
                self, "Resolution Warning",
                f"Image is {pix.width()}×{pix.height()} — max allowed: {CANVAS_W}×{CANVAS_H}.\n"
                "It will be scaled to fit."
            )
        self._bg_path = path
        self.canvas.set_background(pix)
        fname = os.path.basename(path)
        self.ui.label.setText(fname)
        self._iwf_data["bkground"] = fname
        # Add to resources too
        self._add_file_to_resources(path)
        self._update_json_tree()
        self.ui.statusbar.showMessage(f"Background loaded: {fname}")

    def _clear_background(self):
        self._bg_path = None
        self.canvas.set_background(None)
        self.ui.label.setText("No background uploaded")
        self._iwf_data["bkground"] = "image.bmp"
        self._update_json_tree()
        self.ui.statusbar.showMessage("Background cleared.")

    # ── JSON Tree ──────────────────────────────────────────────────────────

    def _update_json_tree(self):
        """Update the tree widget with current iwf data"""
        self.ui.treeWidget.clear()
        self._populate_tree(self.ui.treeWidget.invisibleRootItem(), self._iwf_data)
        self.ui.treeWidget.expandAll()

    def _populate_tree(self, parent_item, obj, key_name=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                child = QTreeWidgetItem(parent_item, [str(k), ""])
                child.setForeground(0, QColor("#00bcd4"))
                self._populate_tree(child, v, str(k))
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                child = QTreeWidgetItem(parent_item, [f"[{i}]", ""])
                child.setForeground(0, QColor("#79c0ff"))
                self._populate_tree(child, v, f"[{i}]")
        else:
            parent_item.setText(1, str(obj) if obj is not None else "null")
            parent_item.setForeground(1, QColor("#a5d6ff") if isinstance(obj, str) else QColor("#ffa657"))

    def _show_raw_json(self):
        """Show raw JSON editor dialog"""
        dlg = RawJsonDialog(self._iwf_data, self)
        if dlg.exec():
            new_data = dlg.get_data()
            if new_data is not None:
                self._iwf_data = new_data
                self._update_json_tree()
                self.ui.statusbar.showMessage("JSON updated from raw editor")

    # ── Project Management ─────────────────────────────────────────────────

    def _new_dial(self):
        reply = QMessageBox.question(
            self, "New Dial",
            "Start a new dial? All unsaved changes will be lost.",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self._iwf_data = copy.deepcopy(SKELETON_IWF)
            self._bg_path = None
            self._hand_filenames = {}
            self.canvas.set_background(None)
            for h in ("hour", "minute", "second"):
                self.canvas.set_hand(h, None)
            self.canvas.set_angles(0, 0, 0)
            self.ui.label.setText("No background uploaded")
            self._reset_rotations()
            # Reset spinboxes
            self.ui.spinBoxHourCenterX.setValue(0)
            self.ui.spinBoxHourCenterY.setValue(0)
            self.ui.spinBoxMinCenterX.setValue(0)
            self.ui.spinBoxMinCenterY.setValue(0)
            self.ui.spinBoxSecCenterX.setValue(0)
            self.ui.spinBoxSecCenterY.setValue(0)
            self.ui.spinBoxHourAnchorX.setValue(120)
            self.ui.spinBoxHourAnchorY.setValue(142)
            self.ui.spinBoxMinAnchorX.setValue(120)
            self.ui.spinBoxMinAnchorY.setValue(142)
            self.ui.spinBoxSecAnchorX.setValue(120)
            self.ui.spinBoxSecAnchorY.setValue(142)
            self._update_json_tree()
            self.ui.statusbar.showMessage("New dial created.")

    def _open_project(self):
        folder = QFileDialog.getExistingDirectory(self, "Open Project Folder")
        if not folder:
            return
        iwf_path = os.path.join(folder, "iwf.json")
        if not os.path.exists(iwf_path):
            QMessageBox.warning(self, "Not Found", "No iwf.json found in selected folder.")
            return
        try:
            with open(iwf_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._iwf_data = data

            # Load background if present
            bg_name = data.get("bkground", "image.bmp")
            bg_path = os.path.join(folder, bg_name)
            if os.path.exists(bg_path):
                pix = QPixmap(bg_path)
                if not pix.isNull():
                    self.canvas.set_background(pix)
                    self.ui.label.setText(bg_name)
                    self._bg_path = bg_path
                    self._add_file_to_resources(bg_path)

            # Load hands from watch item
            items = data.get("item", [])
            watch_item = next((it for it in items if it.get("widget") == "watch"), None)
            if watch_item:
                # Load hand images
                for hand in ["hour", "minute", "second"]:
                    fname = watch_item.get(hand, "")
                    if fname:
                        hand_path = os.path.join(folder, fname)
                        if os.path.exists(hand_path):
                            pix = QPixmap(hand_path)
                            if not pix.isNull():
                                self.canvas.set_hand(hand, pix)
                                self._hand_filenames[hand] = fname
                                self._add_file_to_resources(hand_path)
                                self._update_hand_thumb(hand, pix)

                # Load center/anchor values
                self.ui.spinBoxHourCenterX.setValue(watch_item.get("hourcenterx", 0))
                self.ui.spinBoxHourCenterY.setValue(watch_item.get("hourcentery", 0))
                self.ui.spinBoxMinCenterX.setValue(watch_item.get("mincenterx", 0))
                self.ui.spinBoxMinCenterY.setValue(watch_item.get("mincentery", 0))
                self.ui.spinBoxSecCenterX.setValue(watch_item.get("seccenterx", 0))
                self.ui.spinBoxSecCenterY.setValue(watch_item.get("seccentery", 0))
                self.ui.spinBoxHourAnchorX.setValue(watch_item.get("houranchorx", 120))
                self.ui.spinBoxHourAnchorY.setValue(watch_item.get("houranchory", 142))
                self.ui.spinBoxMinAnchorX.setValue(watch_item.get("minanchorx", 120))
                self.ui.spinBoxMinAnchorY.setValue(watch_item.get("minanchory", 142))
                self.ui.spinBoxSecAnchorX.setValue(watch_item.get("secanchorx", 120))
                self.ui.spinBoxSecAnchorY.setValue(watch_item.get("secanchory", 142))

                self._update_canvas_coords()

            self._update_json_tree()
            self.ui.statusbar.showMessage(f"Project loaded from: {folder}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open project:\n{e}")

    def _save_iwf(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Save iwf.json", "iwf.json", "JSON Files (*.json)"
        )
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self._iwf_data, f, indent=2, newline="\r\n", ensure_ascii=False) # VeryFit app only supports CRLF
            self.ui.statusbar.showMessage(f"iwf.json saved → {path}")
            QMessageBox.information(self, "Saved", f"iwf.json saved to:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save:\n{e}")

    # ── Stub Functions (to be implemented later) ───────────────────────────

    def _save_font_json(self):
        """Stub - Save font.json functionality to be implemented later"""
        QMessageBox.information(self, "Coming Soon", "font.json export will be implemented in a future update.")

    def _validate(self, json_only: bool = False):
        """Stub - Validation functionality to be implemented later"""
        QMessageBox.information(self, "Coming Soon", "Validation features will be implemented in a future update.")

    def _validate_font_json(self):
        """Stub - Validate font.json functionality to be implemented later"""
        QMessageBox.information(self, "Coming Soon", "font.json validation will be implemented in a future update.")

    def _show_about(self):
        """Show about dialog"""
        QMessageBox.about(self, "About IDW26 Dial Creator",
            "IDW26 Dial Creator\n\n"
            "Watch Face Tool for VRPEFIT IDW26 Smartwatch\n\n"
            "Built with Python & PySide6")

    def _export_iwf_stub(self):
        """Stub - Export .iwf functionality to be implemented later"""
        QMessageBox.information(self, "Coming Soon", ".iwf binary export will be implemented in a future update.")

    def _export_iwf_lz_stub(self):
        """Stub - Export .iwf.lz functionality to be implemented later"""
        QMessageBox.information(self, "Coming Soon", ".iwf.lz compressed export will be implemented in a future update.")

    def _export_entire_dial_stub(self):
        """Stub - Export entire dial functionality to be implemented later"""
        QMessageBox.information(self, "Coming Soon", "Full dial export with resources will be implemented in a future update.")


class RawJsonDialog(QDialog):
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Raw iwf.json Editor")
        self.setMinimumSize(600, 500)
        self.setStyleSheet(parent.styleSheet() if parent else "")
        self._data = None

        layout = QVBoxLayout(self)
        self.editor = QTextEdit()
        self.editor.setFont(QFont("Consolas", 11))
        self.editor.setPlainText(json.dumps(data, indent=2, ensure_ascii=False))
        layout.addWidget(self.editor)

        btn_row = QHBoxLayout()
        self.ok_btn = QPushButton("Apply")
        self.ok_btn.setObjectName("primaryBtn")
        self.cancel_btn = QPushButton("Cancel")
        btn_row.addStretch()
        btn_row.addWidget(self.ok_btn)
        btn_row.addWidget(self.cancel_btn)
        layout.addLayout(btn_row)

        self.ok_btn.clicked.connect(self._apply)
        self.cancel_btn.clicked.connect(self.reject)

    def _apply(self):
        try:
            self._data = json.loads(self.editor.toPlainText())
            self.accept()
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "JSON Error", str(e))

    def get_data(self) -> dict | None:
        return self._data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_CYAN_STYLESHEET)

    # Initialize families with a default value before potential font loading
    families = ["Segoe UI", "Arial"]  # Default fallback fonts

    # Load custom font
    base_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(base_dir, "MiSans-Demibold.ttf")

    if os.path.exists(font_path):
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print(f"Failed to load font: {font_path}")
        else:
            families = QFontDatabase.applicationFontFamilies(font_id)
            print(f"Loaded font: {families}")
    else:
        print(f"Font file not found: {font_path}")

    # Set font for the application
    if families and families[0]:
        font = QFont(families[0], 10)
        font.setStyleStrategy(
            QFont.StyleStrategy.PreferAntialias |
            QFont.StyleStrategy.PreferQuality
        )
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        app.setFont(font)

    app.setStyle("Fusion")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())