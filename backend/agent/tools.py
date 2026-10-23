from langchain_core.tools import tool
from rag.llm import extract_text, get_llm
from logger import GLOBAL_LOGGER as log


# INTERNAL LLM HELPER

def _ask_llm(prompt: str) -> str:
    """Invoke the configured LLM and return the text content."""
    try:
        response = get_llm().invoke(prompt)
        return extract_text(response.content)
    except Exception as e:
        return f"LLM_ERROR: {str(e)}"



# Agent 1 Tools: Risk & Compliance

@tool
def check_sanctions_list(vendor_name: str) -> str:
    """Checks if a vendor is on global restricted/sanctioned entities lists."""
    prompt = f"""You are a compliance screening system. Your job is to check whether the 
vendor name below appears on any major global sanctions or restricted-entity lists based 
on your training knowledge.

Check against these lists:
- US OFAC SDN (Specially Designated Nationals) List
- EU Consolidated Sanctions List
- UN Security Council Sanctions List
- UK HMT Sanctions List
- Any other major international sanctions or embargo lists

Vendor to screen: "{vendor_name}"

INSTRUCTIONS:
- If the vendor name matches or closely resembles ANY known sanctioned entity, respond 
  with: RED ALERT: [reason and which list they appear on]
- If the vendor is NOT found on any known sanctions list, respond with: 
  CLEARED: Vendor not found on known global sanctions lists.
- If the name is suspicious or could be a shell company for a sanctioned entity, note 
  that concern.
- Be precise. Do not fabricate matches — only flag if you have genuine knowledge.

Respond in a single concise paragraph starting with either "RED ALERT:" or "CLEARED:"."""

    result = _ask_llm(prompt)
    if result.startswith("LLM_ERROR"):
        return f"SYSTEM WARNING: Sanctions check unavailable — {result}. Manual review required."
    return result
