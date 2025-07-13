# Pixell Agent Cloud API Documentation

Base URL: `https://main.d2o02924ohm5pe.amplifyapp.com/api`
Local URL: `http://localhost:4000/api`

## Authentication

All API endpoints (except auth endpoints) require authentication via:
1. **Session Cookie**: Automatically set after login
2. **API Key**: Pass as `Authorization: Bearer YOUR_API_KEY` header

## API Endpoints

### 1. Authentication

#### POST /api/auth/login
Login with email and password.

**Request:**
```bash
curl -X POST http://localhost:4000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123",
    "rememberMe": false
  }'
```

**Response:**
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "created_at": "2024-01-01T00:00:00Z"
  },
  "session": {
    "access_token": "eyJhbGc...",
    "refresh_token": "eyJhbGc...",
    "expires_in": 3600
  }
}
```

#### POST /api/auth/signup
Create a new account.

**Request:**
```bash
curl -X POST http://localhost:4000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newuser@example.com",
    "password": "password123",
    "organizationName": "My Company"
  }'
```

**Response:**
```json
{
  "message": "Please check your email to verify your account",
  "user": {
    "id": "uuid",
    "email": "newuser@example.com"
  }
}
```

#### POST /api/auth/logout
Logout current user.

**Request:**
```bash
curl -X POST http://localhost:4000/api/auth/logout \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "message": "Logged out successfully"
}
```

#### GET /api/auth/session
Get current session info.

**Request:**
```bash
curl http://localhost:4000/api/auth/session \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  },
  "organization": {
    "id": "uuid",
    "name": "My Company",
    "credits": 1000
  }
}
```

### 2. Organizations

#### GET /api/organizations/current
Get current user's organization.

**Request:**
```bash
curl http://localhost:4000/api/organizations/current \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "organization": {
    "id": "uuid",
    "name": "My Company",
    "credits": 1000,
    "created_at": "2024-01-01T00:00:00Z"
  },
  "role": "owner"
}
```

#### PATCH /api/organizations/current
Update organization details.

**Request:**
```bash
curl -X PATCH http://localhost:4000/api/organizations/current \
  -H "Cookie: sb-xxx-auth-token=..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Company Name"
  }'
```

**Response:**
```json
{
  "organization": {
    "id": "uuid",
    "name": "New Company Name",
    "credits": 1000,
    "updated_at": "2024-01-01T00:00:00Z"
  }
}
```

#### GET /api/organizations/members
Get organization members.

**Request:**
```bash
curl http://localhost:4000/api/organizations/members \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "members": [
    {
      "id": "uuid",
      "user_id": "uuid",
      "email": "user@example.com",
      "role": "owner",
      "joined_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### POST /api/organizations/members
Invite a new member.

**Request:**
```bash
curl -X POST http://localhost:4000/api/organizations/members \
  -H "Cookie: sb-xxx-auth-token=..." \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newmember@example.com",
    "role": "member"
  }'
```

**Response:**
```json
{
  "invitation": {
    "id": "uuid",
    "email": "newmember@example.com",
    "role": "member",
    "expires_at": "2024-01-08T00:00:00Z"
  }
}
```

#### DELETE /api/organizations/members/:userId
Remove a member.

**Request:**
```bash
curl -X DELETE http://localhost:4000/api/organizations/members/user-uuid \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "message": "Member removed successfully"
}
```

### 3. API Keys

#### GET /api/api-keys
List all API keys.

**Request:**
```bash
curl http://localhost:4000/api/api-keys \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "apiKeys": [
    {
      "id": "uuid",
      "name": "Production Key",
      "key_preview": "sk_live_abc123...",
      "last_used_at": "2024-01-01T00:00:00Z",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### POST /api/api-keys
Create a new API key.

**Request:**
```bash
curl -X POST http://localhost:4000/api/api-keys \
  -H "Cookie: sb-xxx-auth-token=..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Development Key"
  }'
```

**Response:**
```json
{
  "apiKey": {
    "id": "uuid",
    "name": "Development Key",
    "key": "sk_live_abcdefghijklmnopqrstuvwxyz123456",
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

#### DELETE /api/api-keys/:id
Delete an API key.

**Request:**
```bash
curl -X DELETE http://localhost:4000/api/api-keys/key-uuid \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "message": "API key deleted successfully"
}
```

#### POST /api/api-keys/:id/rotate
Rotate an API key.

**Request:**
```bash
curl -X POST http://localhost:4000/api/api-keys/key-uuid/rotate \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "apiKey": {
    "id": "uuid",
    "name": "Development Key",
    "key": "sk_live_newkey789xyz",
    "rotated_at": "2024-01-01T00:00:00Z"
  }
}
```

### 4. Agent Apps

#### GET /api/agent-apps
List all agent apps.

**Request:**
```bash
curl http://localhost:4000/api/agent-apps \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "apps": [
    {
      "id": "uuid",
      "name": "Customer Support Bot",
      "description": "AI-powered customer support",
      "is_public": false,
      "created_at": "2024-01-01T00:00:00Z",
      "packages": [
        {
          "id": "uuid",
          "version": "1.0.0",
          "created_at": "2024-01-01T00:00:00Z"
        }
      ]
    }
  ]
}
```

#### POST /api/agent-apps
Create a new agent app.

**Request:**
```bash
curl -X POST http://localhost:4000/api/agent-apps \
  -H "Cookie: sb-xxx-auth-token=..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My New Agent",
    "description": "Description of my agent",
    "is_public": false
  }'
```

**Response:**
```json
{
  "app": {
    "id": "uuid",
    "name": "My New Agent",
    "description": "Description of my agent",
    "is_public": false,
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

#### GET /api/agent-apps/:id
Get a specific agent app.

**Request:**
```bash
curl http://localhost:4000/api/agent-apps/app-uuid \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "app": {
    "id": "uuid",
    "name": "Customer Support Bot",
    "description": "AI-powered customer support",
    "is_public": false,
    "created_at": "2024-01-01T00:00:00Z",
    "packages": [
      {
        "id": "uuid",
        "version": "1.0.0",
        "s3_url": "https://s3.amazonaws.com/...",
        "size": 1024000,
        "created_at": "2024-01-01T00:00:00Z"
      }
    ]
  }
}
```

#### PATCH /api/agent-apps/:id
Update an agent app.

**Request:**
```bash
curl -X PATCH http://localhost:4000/api/agent-apps/app-uuid \
  -H "Cookie: sb-xxx-auth-token=..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Agent Name",
    "description": "Updated description",
    "is_public": true
  }'
```

**Response:**
```json
{
  "app": {
    "id": "uuid",
    "name": "Updated Agent Name",
    "description": "Updated description",
    "is_public": true,
    "updated_at": "2024-01-01T00:00:00Z"
  }
}
```

#### DELETE /api/agent-apps/:id
Delete an agent app.

**Request:**
```bash
curl -X DELETE http://localhost:4000/api/agent-apps/app-uuid \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "message": "Agent app deleted successfully"
}
```

### 5. Packages

#### POST /api/agent-apps/:id/packages
Upload a new package.

**Request:**
```bash
curl -X POST http://localhost:4000/api/agent-apps/app-uuid/packages \
  -H "Cookie: sb-xxx-auth-token=..." \
  -F "file=@agent.apkg" \
  -F "version=1.0.1"
```

**Response:**
```json
{
  "package": {
    "id": "uuid",
    "version": "1.0.1",
    "s3_url": "https://s3.amazonaws.com/...",
    "size": 2048000,
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

#### POST /api/agent-apps/:id/packages/deploy
Deploy a package to the runtime (with validation and credit deduction).

**Request:**
```bash
# Using session authentication
curl -X POST http://localhost:4000/api/agent-apps/app-uuid/packages/deploy \
  -H "Cookie: sb-xxx-auth-token=..." \
  -F "file=@agent.apkg" \
  -F "version=1.2.0" \
  -F "release_notes=Fixed bugs and improved performance" \
  -F "signature=@agent.apkg.sig"

# Using API key authentication
curl -X POST http://localhost:4000/api/agent-apps/app-uuid/packages/deploy \
  -H "Authorization: Bearer pac_your_api_key_here" \
  -F "file=@agent.apkg" \
  -F "version=1.2.0"
```

**Response (202 Accepted):**
```json
{
  "deployment": {
    "id": "deployment-uuid",
    "status": "queued",
    "message": "Deployment queued successfully",
    "queued_at": "2024-01-01T00:00:00Z",
    "estimated_duration_seconds": 120
  },
  "package": {
    "id": "package-uuid",
    "version": "1.2.0",
    "size_bytes": 2048000,
    "status": "uploading"
  },
  "tracking": {
    "status_url": "https://your-app.com/api/deployments/deployment-uuid",
    "webhook_url": "https://your-app.com/api/agent-apps/app-uuid/webhooks"
  }
}
```

**Error Responses:**

400 Bad Request - Package validation failed:
```json
{
  "error": "Package validation failed",
  "details": [
    "Invalid APKG format",
    "Missing required manifest.json",
    "Version already exists"
  ]
}
```

401 Unauthorized - Authentication failed:
```json
{
  "error": "Invalid API key or session"
}
```

402 Payment Required - Insufficient credits:
```json
{
  "error": "Insufficient credits",
  "required": 10,
  "available": 5
}
```

**Notes:**
- File size is used to calculate credit cost (1 credit per MB)
- Package is validated before deployment
- Credits are reserved during deployment and refunded if deployment fails
- Use the status URL to track deployment progress

#### GET /api/agent-apps/:id/packages
List all packages for an agent app.

**Request:**
```bash
curl http://localhost:4000/api/agent-apps/app-uuid/packages \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "packages": [
    {
      "id": "uuid",
      "version": "1.0.1",
      "s3_url": "https://s3.amazonaws.com/...",
      "size": 2048000,
      "created_at": "2024-01-01T00:00:00Z"
    },
    {
      "id": "uuid",
      "version": "1.0.0",
      "s3_url": "https://s3.amazonaws.com/...",
      "size": 1024000,
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### DELETE /api/agent-apps/:id/packages/:packageId
Delete a package.

**Request:**
```bash
curl -X DELETE http://localhost:4000/api/agent-apps/app-uuid/packages/package-uuid \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "message": "Package deleted successfully"
}
```

### 6. Credits & Billing

#### GET /api/credits/balance
Get current credit balance.

**Request:**
```bash
curl http://localhost:4000/api/credits/balance \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "credits": 1000,
  "usage_this_month": 250,
  "last_topped_up": "2024-01-01T00:00:00Z"
}
```

#### POST /api/credits/topup
Create a credit top-up session.

**Request:**
```bash
curl -X POST http://localhost:4000/api/credits/topup \
  -H "Cookie: sb-xxx-auth-token=..." \
  -H "Content-Type: application/json" \
  -d '{
    "package": "starter",
    "credits": 1000
  }'
```

**Response:**
```json
{
  "sessionUrl": "https://checkout.stripe.com/c/pay/cs_live_xxx",
  "sessionId": "cs_live_xxx"
}
```

#### GET /api/credits/history
Get credit transaction history.

**Request:**
```bash
curl http://localhost:4000/api/credits/history \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "transactions": [
    {
      "id": "uuid",
      "type": "purchase",
      "amount": 1000,
      "balance_after": 2000,
      "description": "Credit top-up",
      "created_at": "2024-01-01T00:00:00Z"
    },
    {
      "id": "uuid",
      "type": "usage",
      "amount": -10,
      "balance_after": 1990,
      "description": "Agent invocation",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

### 7. Usage & Metrics

#### GET /api/usage/metrics
Get usage metrics summary.

**Request:**
```bash
curl http://localhost:4000/api/usage/metrics \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "invocations": 15420,
  "invocationsChange": 12.5,
  "packagesUploaded": 45,
  "packagesChange": 8.0,
  "apiCalls": 28750,
  "apiCallsChange": -5.2,
  "creditsUsed": 3250,
  "creditsChange": 15.8
}
```

#### GET /api/usage/chart
Get usage chart data.

**Request:**
```bash
curl http://localhost:4000/api/usage/chart?days=30 \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "data": [
    {
      "date": "Jan 01",
      "invocations": 125,
      "credits": 45
    },
    {
      "date": "Jan 02",
      "invocations": 189,
      "credits": 67
    }
  ]
}
```

#### GET /api/usage/activity
Get recent activity.

**Request:**
```bash
curl http://localhost:4000/api/usage/activity?limit=20 \
  -H "Cookie: sb-xxx-auth-token=..."
```

**Response:**
```json
{
  "events": [
    {
      "id": "uuid",
      "type": "invocation",
      "description": "Agent 'Customer Support Bot' invoked",
      "value": 10,
      "timestamp": "2024-01-01T12:00:00Z"
    },
    {
      "id": "uuid",
      "type": "package_upload",
      "description": "Uploaded version 1.0.1 of 'Data Analyzer'",
      "timestamp": "2024-01-01T11:30:00Z"
    }
  ]
}
```

#### POST /api/usage/export
Export usage data.

**Request:**
```bash
curl -X POST http://localhost:4000/api/usage/export \
  -H "Cookie: sb-xxx-auth-token=..." \
  -H "Content-Type: application/json" \
  -d '{
    "format": "csv",
    "startDate": "2024-01-01",
    "endDate": "2024-01-31"
  }'
```

**Response:**
```json
{
  "downloadUrl": "https://s3.amazonaws.com/exports/usage-export-xxx.csv",
  "expiresAt": "2024-01-02T00:00:00Z"
}
```

### 8. Webhooks

#### POST /api/stripe/webhook
Stripe webhook endpoint (called by Stripe).

**Request:**
```bash
curl -X POST http://localhost:4000/api/stripe/webhook \
  -H "Stripe-Signature: t=1234567890,v1=..." \
  -d '{
    "type": "checkout.session.completed",
    "data": {
      "object": {
        "id": "cs_live_xxx",
        "metadata": {
          "userId": "uuid",
          "credits": "1000"
        }
      }
    }
  }'
```

**Response:**
```json
{
  "received": true
}
```

### 9. Deployments

#### GET /api/deployments/:id
Get deployment status and details.

**Request:**
```bash
curl http://localhost:4000/api/deployments/deployment-uuid \
  -H "Authorization: Bearer pac_your_api_key_here"
```

**Response:**
```json
{
  "deployment": {
    "id": "deployment-uuid",
    "status": "processing",
    "package_id": "package-uuid",
    "agent_app_id": "app-uuid",
    "version": "1.2.0",
    "created_at": "2024-01-01T00:00:00Z",
    "started_at": "2024-01-01T00:01:00Z",
    "progress": {
      "current_step": "upload_to_s3",
      "steps": [
        {
          "name": "validate_package",
          "status": "completed",
          "started_at": "2024-01-01T00:01:00Z",
          "completed_at": "2024-01-01T00:01:10Z"
        },
        {
          "name": "upload_to_s3",
          "status": "processing",
          "started_at": "2024-01-01T00:01:10Z"
        },
        {
          "name": "generate_metadata",
          "status": "pending"
        },
        {
          "name": "notify_runtime",
          "status": "pending"
        },
        {
          "name": "finalize",
          "status": "pending"
        }
      ]
    }
  }
}
```

**Status Values:**
- `queued` - Deployment is waiting to be processed
- `processing` - Deployment is being processed
- `completed` - Deployment completed successfully
- `failed` - Deployment failed

#### GET /api/deployments/queue/stats
Get deployment queue statistics.

**Request:**
```bash
curl http://localhost:4000/api/deployments/queue/stats
```

**Response:**
```json
{
  "stats": {
    "queued": 3,
    "processing": 1,
    "completed": 156,
    "failed": 2,
    "total": 162
  },
  "health": {
    "status": "healthy",
    "message": "Queue is operating normally"
  },
  "metrics": {
    "avgProcessingTimeSeconds": 45,
    "lastUpdated": "2024-01-01T00:00:00Z"
  }
}
```

**Health Status Values:**
- `healthy` - Queue operating normally
- `warning` - High queue depth or failure rate
- `critical` - Too many jobs stuck in processing

### 10. Deployment Webhooks

#### GET /api/agent-apps/:id/webhooks
List webhooks for an agent app.

**Request:**
```bash
curl http://localhost:4000/api/agent-apps/app-uuid/webhooks \
  -H "Authorization: Bearer pac_your_api_key_here"
```

**Response:**
```json
{
  "webhooks": [
    {
      "id": "webhook-uuid",
      "url": "https://example.com/webhook",
      "events": ["deployment.completed", "deployment.failed"],
      "active": true,
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### POST /api/agent-apps/:id/webhooks
Create a webhook for deployment events.

**Request:**
```bash
curl -X POST http://localhost:4000/api/agent-apps/app-uuid/webhooks \
  -H "Authorization: Bearer pac_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/webhook",
    "events": ["deployment.completed", "deployment.failed"],
    "secret": "webhook_secret_key"
  }'
```

**Response:**
```json
{
  "webhook": {
    "id": "webhook-uuid",
    "url": "https://example.com/webhook",
    "events": ["deployment.completed", "deployment.failed"],
    "active": true,
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

#### DELETE /api/agent-apps/:id/webhooks/:webhookId
Delete a webhook.

**Request:**
```bash
curl -X DELETE http://localhost:4000/api/agent-apps/app-uuid/webhooks/webhook-uuid \
  -H "Authorization: Bearer pac_your_api_key_here"
```

**Response:**
```json
{
  "message": "Webhook deleted successfully"
}
```

**Webhook Payload Example:**
```json
{
  "event": "deployment.completed",
  "timestamp": "2024-01-01T00:05:00Z",
  "data": {
    "deployment_id": "deployment-uuid",
    "agent_app_id": "app-uuid",
    "package_id": "package-uuid",
    "version": "1.2.0",
    "status": "completed",
    "duration_seconds": 120,
    "s3_url": "https://s3.amazonaws.com/..."
  }
}
```

### 11. Cron Jobs

#### POST /api/cron/process-deployments
Process queued deployments (called by scheduler).

**Request:**
```bash
# Called by AWS EventBridge, Vercel Cron, or external scheduler
curl -X POST http://localhost:4000/api/cron/process-deployments \
  -H "x-cron-secret: your-cron-secret"
```

**Response:**
```json
{
  "processed": true,
  "jobId": "deployment-uuid",
  "status": "completed",
  "duration": 45
}
```

**Response when no jobs:**
```json
{
  "processed": false,
  "message": "No jobs to process"
}
```

**Security:**
- Requires `x-cron-secret` header matching `CRON_SECRET` environment variable
- Returns 401 if secret is invalid or missing

### 12. Health Check

#### GET /api/health
Check API health status.

**Request:**
```bash
curl http://localhost:4000/api/health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00Z",
  "services": {
    "database": "connected",
    "storage": "connected",
    "auth": "operational"
  }
}
```

## Error Responses

All endpoints return consistent error responses:

```json
{
  "error": "Error message",
  "code": "ERROR_CODE",
  "details": {} // Optional additional details
}
```

Common HTTP status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 409: Conflict
- 500: Internal Server Error

## Rate Limiting

API endpoints are rate limited:
- Authenticated requests: 1000 requests per hour
- Unauthenticated requests: 100 requests per hour

Rate limit headers:
- `X-RateLimit-Limit`: Maximum requests allowed
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Time when limit resets (Unix timestamp)