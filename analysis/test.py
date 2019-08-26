response_dictionary = {

    "abp": {
        "title": result.find('title').get_text(),
        "fullimage": result.find('fullimage').get_text(),
        "description": result.find('description').string,
    },
    "news18": {
        "title": result.find('title').get_text(),
        "fullimage": result.find('fullimage').get_text(),
        "description": result.find('description').string,
    },
    "dainikbhaskar": {
        "title": result.find('title').get_text(),
        "fullimage": result.find('fullimage').get_text(),
        "description": result.find('description').string,
    },
    "timeofindia": {
        "title": result.find('title').get_text(),
        "fullimage": result.find('fullimage').get_text(),
        "description": result.find('description').string,
    },

}