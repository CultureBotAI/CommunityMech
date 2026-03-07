# Filter Panel Testing Guide

## Manual Testing Checklist for UMAP Visualization

### 1. Enhanced Search Functionality
- [ ] Open `docs/community_umap.html` in browser
- [ ] Type "AMD" in search box → should highlight ~8 AMD communities
- [ ] Type "Richmond" → should show 1 community (Richmond Mine)
- [ ] Type "acid" → should match environment field and show relevant communities
- [ ] Click clear button (✕) → should reset search and show all 73 communities
- [ ] Search counter should update: "Showing X of 73 communities"

### 2. Category Facet
- [ ] Check "AMD" checkbox → should filter to ~8 AMD communities
- [ ] Check both "AMD" and "DIET" → should show both categories (OR logic)
- [ ] Click "All" button → should check all 14 category boxes
- [ ] Click "None" button → should uncheck all boxes
- [ ] Counts should update dynamically: "AMD (8)", "DIET (6)", etc.

### 3. Ecological State Facet
- [ ] Check "STABLE" → should filter to stable communities
- [ ] Check "ENGINEERED" → should add engineered communities to filter
- [ ] Uncheck boxes → should update visualization immediately

### 4. Origin Facet
- [ ] Check "NATURAL" → should filter to natural communities
- [ ] Check "SYNTHETIC" → should add synthetic communities
- [ ] Multiple selections should work (OR logic)

### 5. Combined Filters (AND logic between facet types)
- [ ] Search "iron" + check "AMD" → should show intersection
- [ ] Search + Category + State → should combine all filters
- [ ] Filtered points should fade to opacity 0.1
- [ ] Visible points should remain at opacity 0.8

### 6. Active Filters Summary
- [ ] Apply any filter → yellow "Active Filters" box should appear
- [ ] Should show removable tags: "Search: term", "Category: AMD", etc.
- [ ] Click ✕ on tag → should remove that specific filter
- [ ] Click "Clear All" button → should reset all filters
- [ ] Summary should hide when no filters active

### 7. Zoom/Pan Preservation
- [ ] Apply filter → zoom in → change filter
- [ ] Verify zoom level is preserved (no reset to default view)
- [ ] Pan to different area → apply filter → verify pan preserved

### 8. Facet Collapse/Expand
- [ ] Click on "Category" header → should collapse facet (show + icon)
- [ ] Click again → should expand facet (show − icon)
- [ ] Same for "Ecological State" and "Origin" facets

### 9. Responsive Layout
- [ ] Resize browser to < 1200px width
- [ ] Filter panel should move above plot (vertical stacking)
- [ ] All functionality should still work

### 10. Color/Size Controls Compatibility
- [ ] Change "Color by" dropdown → filters should persist
- [ ] Change "Size by" dropdown → filters should persist
- [ ] Filtered state should be maintained after visualization updates

### 11. Performance
- [ ] Typing in search should have ~150ms debounce (smooth, no lag)
- [ ] Checking/unchecking facets should update instantly
- [ ] No JavaScript errors in browser console (F12)

### 12. Counts and Statistics
- [ ] Initial load: "Showing 73 of 73 communities"
- [ ] After filtering: counts should accurately reflect visible communities
- [ ] Facet counts should update based on current filter state
- [ ] All counts should be consistent and accurate

## Browser Compatibility
Test in:
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari

## Expected Results Summary

**Initial State:**
- 73 communities visible
- All facets expanded with counts
- No active filters
- Search bar empty

**After Filtering:**
- Filtered points at opacity 0.1 (nearly invisible)
- Visible points at opacity 0.8 (normal)
- Active filters summary visible with yellow background
- Dynamic count updates
- Removable filter tags

**User Experience:**
- Smooth, responsive filtering
- No page reloads
- Zoom/pan state preserved
- Clear visual feedback
- Intuitive controls
