def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    merged = []
    for req in requests:
        user_id = req["user_id"]
        online = req["online_features"]

        combined = dict(defaults)
        if user_id in feature_store:
            combined.update(feature_store[user_id])
        
        combined.update(online)
        merged.append(combined)
    return merged

