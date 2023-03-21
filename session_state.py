class _SessionState:
    def __init__(self):
        self.data = None

    def get_data(self):
        return self.data

    def set_data(self, value):
        self.data = value


def get_state():
    from streamlit.report_thread import get_report_ctx
    from streamlit.server.server import Server

    ctx = get_report_ctx()
    session_id = ctx.session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Could not get session info.")

    if not hasattr(session_info, "session_state"):
        session_info.session_state = _SessionState()

    return session_info.session_state
