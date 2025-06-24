function(event, emit)
  local message = event.log.message or ""

  if type(message) ~= "string" or message == "" then
    return
  end

  -- print("Processing line: [" .. message .. "]")

  local is_error = string.match(message, "^ERROR%s+")
  local is_info = string.match(message, "^INFO%s+")
  local is_warn = string.match(message, "^WARN%s+")
  local is_debug = string.match(message, "^DEBUG%s+")
  local is_trace = string.match(message, "^TRACE%s+")
  local is_fatal = string.match(message, "^FATAL%s+")
  
  local is_start = (is_error or is_info or is_warn or is_debug or is_trace or is_fatal)

  if is_start then
    -- print("--- [" .. message .. "] matches start_pattern ---")
    if state.pending_event then
      emit(state.pending_event)
    end

    state.pending_event = event
  else
    if state.pending_event then
      state.pending_event.log.message = state.pending_event.log.message .. "\n" .. message
    end
  end

  return
end