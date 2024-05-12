class Urls:
    ELEMENTS = 'elements'
    TEXT_BOX = 'text-box'
    CHECKBOX = 'checkbox'
    RADIO_BUTTON = 'radio-button'
    WEB_TABLES = 'webtables'
    BUTTONS = 'buttons'
    LINKS = 'links'
    BROKEN_LINKS = 'broken'
    UPLOAD_DOWNLOAD = 'upload-download'
    DYNAMIC_PROPERTIES = 'dynamic-properties'

    FORMS = 'forms'
    PRACTICE_FORM = 'automation-practice-form'

    ALERTS_WINDOWS = 'alertsWindows'
    BROWSER_WINDOWS = 'browser-windows'
    ALERTS = 'alerts'
    FRAMES = 'frames'
    NESTED_FRAMES = 'nestedframes'
    MODAL_DIALOG = 'modal-dialogs'

    WIDGETS = 'widgets'
    ACCORDIAN = 'accordian'
    AUTO_COMPLETE = 'auto-complete'
    DATE_PICKER = 'date-picker'
    SLIDER = 'slider'
    PROGRESS_BAR = 'progress-bar'
    TABS = 'tabs'
    TOOL_TIPS = 'tool-tips'
    MENU = 'menu'
    SELECT_MENU = 'select-menu'

    INTERACTIONS = 'interaction'
    SORTABLE = 'sortable'
    SELECTABLE = 'selectable'
    RESIZEBLE = 'resizable'
    DROPPABLE = 'droppable'
    DRAGABBLE = 'dragabble'

    BOOKS = 'books'

    def __init__(self):
        self._demoqa_host = 'https://demoqa.com/'

    @property
    def demoqa_host(self):
        return self._demoqa_host

urls = Urls()