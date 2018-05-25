# from flask import jsonify, request
# from app.center import center_api
# from app.models import Center


# @center_api.route('/centers', methods = ['GET'])
# def get_all_centers(self):
#   return jsonify(Center.query.all())

# @center_api.route('/centers', methods = ['POST'])
# def create_center(self):
#   center = request.get_json() 
#   if not center['center_name']:
#     return jsonify({
#       'success': 'false',
#       'message': 'center name is requrired'
#     }), 400
#   elif not center['center_location']:
#     return jsonify({
#       'success': 'false',
#       'message': 'center location ks requrired'
#     }), 400

#   elif not center['center_capacity']:
#     return ({
#       'success': 'false',
#       'message': 'center capaxcity is requrired'
#     }), 400
#   return jsonify(center), 200

#   @center_api.route('/centers<int:centerId>', methods = ['GET'])
#   def get_single_center(self):
#     return ''

#   @center_api.route('/centers/<int:centerId', methods = ['PUT'])
#   def modify_center(self):
#     return ''